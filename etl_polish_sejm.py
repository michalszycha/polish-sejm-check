import sys

from mp.EtlMp import prepare_mp
from sitting.EtlSitting import prepare_sittings
from voting.EtlVoting import prepare_voting, prepare_voting_per_mp
from utils.Cache import cache_value
from voting.transform.VotingTransform import add_vote_option_count
import config.config as config

if len(sys.argv) == 2:
    config.term = sys.argv[1]


def main():
    sittings = cache_value("sittings", f"term{config.term}", prepare_sittings)
    voting = prepare_voting(sittings)
    voting_per_mp = cache_value("voting_per_mp", f"term{config.term}", prepare_voting_per_mp, voting)
    cache_value("voting", f"term{config.term}", add_vote_option_count, voting, voting_per_mp)
    cache_value("mps", f"term{config.term}", prepare_mp, voting_per_mp)


if __name__ == "__main__":
    main()
