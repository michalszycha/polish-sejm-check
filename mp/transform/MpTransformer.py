import pandas as pd
import json


def drop_unused_columns(mps: pd.DataFrame) -> pd.DataFrame:
    mps = mps.drop('firstLastName', axis=1)
    mps = mps.drop('lastFirstName', axis=1)
    mps = mps.drop('email', axis=1)
    return mps


def add_percent_of_voting(mps: pd.DataFrame, voting: pd.DataFrame) -> pd.DataFrame:
    """if type(voting['votes'][0]) == str:
        data = voting['votes'].apply(lambda x: json.loads(x.replace("'", '"')))
    else:
        data = voting['votes']
    flattened_data = [item for sublist in data for item in sublist]
    df = pd.DataFrame(flattened_data)"""
    absent_count_per_mp = voting[voting['vote'] == 'ABSENT'].groupby('MP').size()
    total_counts = voting.groupby('MP').size()
    percentages = (100 - (absent_count_per_mp / total_counts * 100)).fillna(100).apply(lambda x: round(x, 2))
    percentages.reset_index(drop=True, inplace=True)
    mps['percentOfVoting'] = percentages
    return mps


def change_column_order(mps: pd.DataFrame) -> pd.DataFrame:
    return mps[
        [
            'id',
            'firstName',
            'lastName',
            'birthDate',
            'birthLocation',
            'educationLevel',
            'profession',
            'club',
            'districtNum',
            'districtName',
            'voivodeship',
            'numberOfVotes',
            'active',
            'inactiveCause',
            'waiverDesc',
            'percentOfVoting',
        ]
    ]

