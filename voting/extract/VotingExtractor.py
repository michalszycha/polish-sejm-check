import pandas as pd
import requests


def get_voting_list(proceedings: pd.Series) -> list:
    data = []
    for proceeding in proceedings:
        url = f"https://api.sejm.gov.pl/sejm/term10/votings/{proceeding}"
        request = requests.get(url)
        request_json = request.json()
        data.append(request_json)
    voting_list = [item for sublist in data for item in sublist]
    return voting_list
