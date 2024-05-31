import pandas as pd
import requests


def get_voting(sittings: pd.Series) -> pd.DataFrame:
    data = []
    for sitting in sittings:
        url = f"https://api.sejm.gov.pl/sejm/term10/votings/{sitting}"
        request = requests.get(url)
        request_json = request.json()
        if request_json:
            voting_numbers = pd.DataFrame(request_json)['votingNumber'].tolist()
            for voting_number in voting_numbers:
                url = f"https://api.sejm.gov.pl/sejm/term10/votings/{sitting}/{voting_number}"
                print(url)
                request = requests.get(url)
                request_json = request.json()
                data.append(request_json)
    return pd.DataFrame(data)
