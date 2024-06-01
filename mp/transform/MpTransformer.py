import pandas as pd


def add_percent_of_voting(mps: pd.DataFrame, voting: pd.DataFrame) -> pd.DataFrame:
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

