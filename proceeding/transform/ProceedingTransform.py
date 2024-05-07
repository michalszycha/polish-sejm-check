import pandas as pd


def transform_proceedings(proceedings: pd.DataFrame) -> pd.DataFrame:
    proceedings = proceedings.query('number != 0')
    proceedings = proceedings.drop('title', axis=1)
    proceedings = proceedings.explode('dates')
    proceedings = proceedings.rename(columns={"dates": "date"})
    return proceedings
