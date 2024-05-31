import requests
import pandas as pd


def get_sittings() -> pd.DataFrame:
    response = requests.get('https://api.sejm.gov.pl/sejm/term10/proceedings')
    data = response.json()
    return pd.DataFrame.from_dict(data)
