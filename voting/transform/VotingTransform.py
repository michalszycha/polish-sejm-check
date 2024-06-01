import multiprocessing
import pandas as pd
import json
from joblib import Parallel, delayed


def add_id_column(voting: pd.DataFrame) -> pd.DataFrame:
    return voting.assign(id=range(1, len(voting) + 1))


# Function to parse JSON strings safely
def parse_json_string(json_str):
    if isinstance(json_str, str):
        json_str = json_str.replace("'", '"')
        return json.loads(json_str)
    return json_str


def map_vote_options(row):
    if isinstance(row['votingOptions'], list):
        option_map = {str(option['optionIndex']): option['option'] for option in row['votingOptions']}
        list_votes = row['votes']['listVotes']
        for option_index, vote_status in list_votes.items():
            if vote_status == 'YES':
                row['votes']['vote'] = option_map.get(option_index, 'Unknown')
                break
    return row


def process_row(row):
    row['votes'] = parse_json_string(row['votes'])
    row['votingOptions'] = parse_json_string(row['votingOptions'])
    return map_vote_options(row)


def get_voting_per_mp(voting: pd.DataFrame) -> pd.DataFrame:
    voting = voting.explode('votes')
    num_cores = min(8, multiprocessing.cpu_count())  # Adjust the number of cores as needed
    voting = pd.concat(Parallel(n_jobs=num_cores)(delayed(process_row)(row) for _, row in voting.iterrows()))
    voting_normalized = pd.json_normalize(voting['votes'])
    voting_normalized['votingId'] = voting['id'].values
    voting_normalized['votingTitle'] = voting['title'].values
    voting_normalized['votingTopic'] = voting['topic'].values
    voting_normalized['votingDescription'] = voting['description'].values
    return voting_normalized


def change_columns_order(voting: pd.DataFrame) -> pd.DataFrame:
    return voting[
        [
            'id',
            'date',
            'sitting',
            'sittingDay',
            'votingNumber',
            'title',
            'topic',
            'description',
            'kind',
            'totalVoted',
            'notParticipating',
            'yes',
            'no',
            'abstain',
            'votingOptions',
            'votes',
        ]
    ]


def change_columns_in_voting_per_mp(voting: pd.DataFrame) -> pd.DataFrame:
    return voting[
        [
            'MP',
            'firstName',
            'lastName',
            'votingId',
            'votingTitle',
            'votingTopic',
            'votingDescription',
            'vote',
        ]
    ]
