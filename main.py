import gevent.monkey
gevent.monkey.patch_all()

from mp.EtlMp import prepare_mp
from proceeding.EtlProceeding import prepare_proceedings
from voting.EtlVoting import prepare_voting



def main():
    proceedings = prepare_proceedings()
    mps = prepare_mp()
    voting = prepare_voting(mps, proceedings)


if __name__ == "__main__":
    main()
