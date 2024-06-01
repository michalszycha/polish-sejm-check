"""import pandas as pd
import requests


def get_voting(sittings: pd.Series) -> pd.DataFrame:
    data = []
    for sitting in sittings:
        url = f"https://api.sejm.gov.pl/sejm/term9/votings/{sitting}"
        request = requests.get(url)
        request_json = request.json()
        if request_json:
            voting_numbers = pd.DataFrame(request_json)['votingNumber'].tolist()
            for voting_number in voting_numbers:
                url = f"https://api.sejm.gov.pl/sejm/term9/votings/{sitting}/{voting_number}"
                print(url)
                request = requests.get(url)
                request_json = request.json()
                data.append(request_json)
    return pd.DataFrame(data)"""

import aiohttp
import asyncio
import pandas as pd
import json


async def fetch_voting(session, sitting, voting_number):
    url = f"https://api.sejm.gov.pl/sejm/term9/votings/{sitting}/{voting_number}"
    async with session.get(url) as response:
        json_str = await response.text()
        json_str = json_str.replace('\\n', '')
        return json.loads(json_str)


async def get_voting(sittings: pd.Series) -> pd.DataFrame:
    data = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for sitting in sittings:
            url = f"https://api.sejm.gov.pl/sejm/term9/votings/{sitting}"
            async with session.get(url) as response:
                request_json = await response.json()
                if request_json:
                    voting_numbers = pd.DataFrame(request_json)['votingNumber'].tolist()
                    for voting_number in voting_numbers:
                        tasks.append(fetch_voting(session, sitting, voting_number))
        results = await asyncio.gather(*tasks)
        data.extend(results)
    return pd.DataFrame(data)
