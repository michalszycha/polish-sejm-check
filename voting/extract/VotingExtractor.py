#import requests
import pandas as pd
import grequests


def get_mp_voting(mp_ids: pd.Series, proceedings: pd.DataFrame):
    data = []
    for mp_id in mp_ids:
        print(mp_id)
        urls = [
            f"https://api.sejm.gov.pl/sejm/term10/MP/{mp_id}/votings/{row['number']}/{row['date']}"
            for index, row in proceedings.iterrows()
        ]
        requests = (grequests.get(url) for url in urls)
        responses = grequests.map(requests)
        # Filter out None responses
        responses = [response for response in responses if response is not None]
        # Convert responses to JSON
        responses_json = [response.json() for response in responses]
        data.append(responses_json)
    return pd.DataFrame.from_dict(data)


def get_mp_voting2(mp_id: int, proceedings: pd.DataFrame):
    print(mp_id)
    urls = [
        f"https://api.sejm.gov.pl/sejm/term10/MP/{mp_id}/votings/{row['number']}/{row['date']}"
        for index, row in proceedings.iterrows()
    ]
    requests = (grequests.get(url) for url in urls)
    responses = grequests.map(requests)

    # Filter out None responses
    responses = [response for response in responses if response is not None]

    # Convert responses to JSON
    responses_json = [response.json() for response in responses]

    return pd.DataFrame.from_dict(responses_json)
