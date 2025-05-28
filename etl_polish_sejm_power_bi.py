import pandas as pd

from mp.EtlMp import prepare_mp
from sitting.EtlSitting import prepare_sittings
from voting.EtlVoting import prepare_voting, prepare_voting_per_mp
from utils.Cache import cache_data
import config.config as config

config.term = "10"

def get_data_for_power_bi():

    sittings_data = cache_data("sittings", f"term{config.term}", prepare_sittings)
    voting_data = cache_data("voting", f"term{config.term}", prepare_voting, sittings_data)
    voting_per_mp_data = cache_data("voting_per_mp", f"term{config.term}", prepare_voting_per_mp, voting_data)
    mps_data = cache_data("mps", f"term{config.term}", prepare_mp, voting_per_mp_data)

    voting_df = pd.DataFrame(voting_data) if not isinstance(voting_data, pd.DataFrame) else voting_data
    voting_per_mp_df = pd.DataFrame(voting_per_mp_data) if not isinstance(voting_per_mp_data,
                                                                          pd.DataFrame) else voting_per_mp_data
    mps_df = pd.DataFrame(mps_data) if not isinstance(mps_data, pd.DataFrame) else mps_data

    # Return all DataFrames as a list
    return [voting_df, voting_per_mp_df, mps_df]


# Call the function to get all your dataframes
all_dfs = get_data_for_power_bi()

# Assign them to variables that Power BI can detect (this is the most important part for PBI)
voting = all_dfs[0]
voting_per_mp = all_dfs[1]
mps = all_dfs[2]
