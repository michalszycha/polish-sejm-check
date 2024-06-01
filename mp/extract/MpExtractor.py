import requests
import pandas as pd


def get_mps() -> pd.DataFrame:
    response = requests.get('https://api.sejm.gov.pl/sejm/term9/MP')
    data = response.json()
    return pd.DataFrame.from_dict(data)
