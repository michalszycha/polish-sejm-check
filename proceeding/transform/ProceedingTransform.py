import pandas as pd


def transform_proceedings(proceedings: pd.DataFrame) -> pd.DataFrame:
    proceedings = proceedings.query('number != 0')
    proceedings = proceedings.drop('title', axis=1)
    return proceedings.explode('dates')
