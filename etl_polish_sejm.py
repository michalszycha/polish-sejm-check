import sys

from mp.EtlMp import prepare_mp
from sitting.EtlSitting import prepare_sittings
from voting.EtlVoting import prepare_voting, prepare_voting_per_mp
from utils.Cache import cache_data
import config.config as config

if len(sys.argv) == 2:
    config.term = sys.argv[1]


def main():
    sittings = cache_data("sittings", f"term{config.term}", prepare_sittings)
    voting = cache_data("voting", f"term{config.term}", prepare_voting, sittings)
    voting_per_mp = cache_data("voting_per_mp", f"term{config.term}", prepare_voting_per_mp, voting)
    cache_data("mps", f"term{config.term}", prepare_mp, voting_per_mp)


if __name__ == "__main__":
    main()
