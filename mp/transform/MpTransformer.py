import pandas as pd


def drop_unused_columns(mps: pd.DataFrame) -> pd.DataFrame:
    mps = mps.drop('firstLastName', axis=1)
    mps = mps.drop('lastFirstName', axis=1)
    mps = mps.drop('email', axis=1)
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
        ]
    ]
