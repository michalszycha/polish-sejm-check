import pandas as pd


def transform_sittings(sittings: pd.DataFrame) -> pd.DataFrame:
    sittings = sittings.query('number != 0')
    sittings = sittings.drop('title', axis=1)
    sittings = sittings.explode('dates')
    sittings = sittings.rename(columns={"dates": "date"})
    return sittings
