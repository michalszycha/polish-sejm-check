from mp.EtlMp import prepare_mp
from sitting.EtlSitting import prepare_sittings
from voting.EtlVoting import prepare_voting, prepare_voting_per_mp
from utils.Cache import cache_value

def main():
    sittings = cache_value("sittings", "term9", prepare_sittings)
    voting = cache_value("voting", "term9_new", prepare_voting, sittings, purge=True)
    #voting_per_mp = cache_value("voting_per_mp", "term9_new", prepare_voting_per_mp, voting)
    #cache_value("mps", "term9", prepare_mp, voting_per_mp, purge=True)


if __name__ == "__main__":
    main()
