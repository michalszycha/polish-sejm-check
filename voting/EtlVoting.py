import pandas as pd
import voting.extract.VotingExtractor as Extract
import utils.Loader as Load
from functools import partial


def prepare_voting(mps: pd.DataFrame, proceedings: pd.DataFrame) -> pd.DataFrame:
    voting = Extract.get_mp_voting(mps['id'], proceedings)
    Load.load_to_csv(voting, "voting")
    #Load.load_to_sql(voting, "voting")
    return voting
