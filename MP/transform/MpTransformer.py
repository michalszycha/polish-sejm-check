import pandas as pd


def drop_unused_columns(mp: pd.DataFrame) -> pd.DataFrame:
    mp = mp.drop('firstLastName', axis=1)
    mp = mp.drop('lastFirstName', axis=1)
    mp = mp.drop('email', axis=1)
    return mp


def change_column_order(mp: pd.DataFrame) -> pd.DataFrame:
    return mp[
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
        ]
    ]
