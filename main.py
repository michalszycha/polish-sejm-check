from mp.EtlMp import prepare_mp
from sitting.EtlSitting import prepare_sittings
from voting.EtlVoting import prepare_voting, prepare_voting_per_mp
from utils.Cache import cache_value


def main():
    sittings = cache_value("sittings", "term10", prepare_sittings, purge=True)
    voting = cache_value("voting", "term10", prepare_voting, sittings, purge=True)
    voting_per_mp = cache_value("voting_per_mp", "term10", prepare_voting_per_mp, voting, purge=True)
    cache_value("mps", "term10", prepare_mp, voting_per_mp, purge=True)


if __name__ == "__main__":
    main()
