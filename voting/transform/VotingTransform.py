import pandas as pd


def add_id_column(voting: pd.DataFrame) -> pd.DataFrame:
    return voting.assign(id=range(1, len(voting) + 1))


def change_column_order(voting: pd.DataFrame) -> pd.DataFrame:
    return voting[
        [
            'id',
            'date',
            'sitting',
            'sittingDay',
            'votingNumber',
            'title',
            'topic',
            'description',
            'kind',
            'totalVoted',
            'notParticipating',
            'yes',
            'no',
            'abstain',
            'votingOptions',
            'votes',
        ]
    ]
