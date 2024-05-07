from MP.EtlMp import prepare_mp
from proceeding.EtlProceeding import prepare_proceedings


def main():
    x = prepare_mp()
    y = prepare_proceedings()
    print(x)
    print(y)


if __name__ == "__main__":
    main()
