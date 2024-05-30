import pandas as pd
import voting.extract.VotingExtractor as Extract


def prepare_voting(proceedings: pd.DataFrame) -> pd.DataFrame:
    voting = Extract.get_voting_list(proceedings['number'])
    return voting
