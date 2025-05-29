import asyncio
import aiohttp
import pandas as pd
import json
import logging  # Added for logging
import time  # For retry delay
# Assuming config.config.py exists and has a 'term' variable
# For example, in config/config.py you might have:
# term = 10
import config.config as config

# --- Logger Setup ---
# Configure basic logging
# You can customize the format, level, and output (e.g., to a file) as needed
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Configuration for retries and concurrency ---
MAX_RETRIES = 3
INITIAL_RETRY_DELAY_SECONDS = 1
CONCURRENCY_LIMIT = 10  # Adjust as needed, start lower if issues persist


async def fetch_voting(session, sitting, voting_number, semaphore):
    url = f"https://api.sejm.gov.pl/sejm/term{config.term}/votings/{sitting}/{voting_number}"
    for attempt in range(MAX_RETRIES):
        try:
            async with semaphore:  # Acquire semaphore before making a request
                logger.debug(f"Attempting to fetch: {url} (Attempt {attempt + 1})")
                async with session.get(url) as response:
                    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
                    # Your original JSON processing:
                    json_str = await response.text()
                    # The replace below might be specific to this API's quirks.
                    # If the API returns standard JSON, response.json() would be cleaner.
                    json_str = json_str.replace('\\n', '')
                    logger.debug(f"Successfully fetched and processed: {url}")
                    return json.loads(json_str)
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:  # Catch a broader range of client-side errors
            if attempt < MAX_RETRIES - 1:
                delay = INITIAL_RETRY_DELAY_SECONDS * (2 ** attempt)  # Exponential backoff
                logger.warning(
                    f"Error fetching {url}: {e}. Retrying in {delay}s... (Attempt {attempt + 1}/{MAX_RETRIES})")
                await asyncio.sleep(delay)
            else:
                logger.error(f"Failed to fetch {url} after {MAX_RETRIES} attempts: {e}")
                return None  # Or raise the exception, or return a specific error structure
    return None  # Should be unreachable if MAX_RETRIES > 0, but good for linters


async def get_voting(sittings) -> pd.DataFrame:  # Type hint changed to be more general
    data = []
    # Define a timeout for the session
    timeout = aiohttp.ClientTimeout(total=60)  # 60 seconds total timeout for a request

    # Create a semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []
        # Changed sittings.items() to enumerate(sittings) to handle numpy arrays and lists
        for sitting_index, sitting in enumerate(sittings):  # Iterate with index for better error reporting if needed
            url_list_votings = f"https://api.sejm.gov.pl/sejm/term{config.term}/votings/{sitting}"
            logger.info(f"Fetching list of votings for sitting: {sitting} (Index: {sitting_index})")
            try:
                async with semaphore:  # Also use semaphore for fetching the list of votings
                    async with session.get(url_list_votings) as response:
                        response.raise_for_status()
                        try:
                            request_json = await response.json()  # Prefer .json() if API returns correct Content-Type
                        except aiohttp.ContentTypeError as cte:
                            # Fallback to text and manual load if Content-Type is not application/json
                            logger.warning(f"ContentTypeError for {url_list_votings}, falling back to text(): {cte}")
                            text_content = await response.text()
                            request_json = json.loads(text_content)

                        if request_json:  # Ensure request_json is not None or empty
                            # Check if request_json is a list of dicts as expected
                            if isinstance(request_json, list) and all(isinstance(item, dict) for item in request_json):
                                voting_df = pd.DataFrame(request_json)
                                if 'votingNumber' in voting_df.columns:
                                    voting_numbers = voting_df['votingNumber'].tolist()
                                    logger.info(
                                        f"Found {len(voting_numbers)} votings for sitting {sitting}. Creating tasks...")
                                    for voting_number in voting_numbers:
                                        tasks.append(fetch_voting(session, sitting, voting_number, semaphore))
                                else:
                                    logger.warning(
                                        f"'votingNumber' column not found in response for sitting {sitting}. Response: {str(request_json[:2]) if isinstance(request_json, list) else str(request_json)}")
                            else:
                                logger.warning(
                                    f"Unexpected JSON structure for sitting {sitting}. Expected list of dicts. Got: {type(request_json)}. Response: {str(request_json[:2]) if isinstance(request_json, list) else str(request_json)}")
                        else:
                            logger.warning(
                                f"No votings found or empty response for sitting {sitting} at {url_list_votings}")
            except (aiohttp.ClientError, asyncio.TimeoutError, json.JSONDecodeError) as e:
                logger.error(f"Error fetching list of votings for sitting {sitting} at {url_list_votings}: {e}")
                # Optionally, decide if you want to skip this sitting or halt everything
                continue  # Skip to the next sitting if fetching the list fails

        if tasks:
            logger.info(f"Gathering results for {len(tasks)} voting details...")
            results = await asyncio.gather(*tasks)
            # Filter out None results from failed fetches if you return None on failure
            data.extend([res for res in results if res is not None])
            logger.info(f"Successfully gathered {len(data)} voting details.")
        else:
            logger.info("No tasks were created to fetch voting details.")

    return pd.DataFrame(data)