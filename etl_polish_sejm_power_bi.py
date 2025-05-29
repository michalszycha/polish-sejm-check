import os
import sys
import logging

cwd = os.getcwd()
logging.basicConfig(filename="log.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info(f"Path: {cwd}")
sys.path.append(cwd)

from mp.EtlMp import prepare_mp
from sitting.EtlSitting import prepare_sittings
from voting.EtlVoting import prepare_voting, prepare_voting_per_mp
import config.config as config

config.term = "10"

def get_data_for_power_bi():

    sittings_data = prepare_sittings()
    voting_data = prepare_voting(sittings_data)
    voting_per_mp_data = prepare_voting_per_mp(voting_data)
    mps_data = prepare_mp(voting_per_mp_data)

    # Return all DataFrames as a list
    return [sittings_data, voting_data, voting_per_mp_data, mps_data]


# Call the function to get all your dataframes
all_dfs = get_data_for_power_bi()

# Assign them to variables that Power BI can detect (this is the most important part for PBI)
sittings = all_dfs[0]
voting = all_dfs[1]
voting_per_mp = all_dfs[2]
mps = all_dfs[3]
