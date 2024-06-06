import requests
import pandas as pd
import config.config as config


def get_sittings() -> pd.DataFrame:
    response = requests.get(f"https://api.sejm.gov.pl/sejm/term{config.term}/proceedings")
    data = response.json()
    return pd.DataFrame.from_dict(data)
