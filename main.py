from mp.EtlMp import prepare_mp
from sitting.EtlSitting import prepare_sittings
from voting.EtlVoting import prepare_voting
from utils.Cache import cache_value


def main():
    sittings = cache_value("sittings", "new", prepare_sittings)
    voting = cache_value("voting", "new", prepare_voting, sittings, purge=True)
    mps = cache_value("mps", "new", prepare_mp, voting, purge=True)


if __name__ == "__main__":
    main()
