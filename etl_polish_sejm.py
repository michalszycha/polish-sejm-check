import sys

from mp.EtlMp import prepare_mp
from sitting.EtlSitting import prepare_sittings
from voting.EtlVoting import prepare_voting, prepare_voting_per_mp
from utils.Cache import cache_value
import config.config as config

if len(sys.argv) == 2:
    config.term = sys.argv[1]


def main():
    sittings = cache_value("sittings", f"term{config.term}", prepare_sittings)
    voting = cache_value("voting", f"term{config.term}", prepare_voting, sittings)
    voting_per_mp = cache_value("voting_per_mp", f"term{config.term}", prepare_voting_per_mp, voting)
    cache_value("mps", f"term{config.term}", prepare_mp, voting_per_mp)


if __name__ == "__main__":
    main()
