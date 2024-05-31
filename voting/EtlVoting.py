import pandas as pd
import voting.extract.VotingExtractor as Extract
import voting.transform.VotingTransform as Transform


def prepare_voting(sittings: pd.DataFrame) -> pd.DataFrame:
    voting = Extract.get_voting(sittings['number'].unique())
    voting = Transform.add_id_column(voting)
    voting = Transform.change_columns_order(voting)
    return voting


def prepare_voting_per_mp(voting: pd.DataFrame) -> pd.DataFrame:
    voting = Transform.get_voting_per_mp(voting)
    voting = Transform.change_columns_in_voting_per_mp(voting)
    return voting
