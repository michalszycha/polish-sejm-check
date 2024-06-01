import pandas as pd
import mp.extract.MpExtractor as Extract
import mp.transform.MpTransformer as Transform


def prepare_mp(voting: pd.DataFrame) -> pd.DataFrame:
    mps = Extract.get_mps()
    mps = Transform.add_percent_of_voting(mps, voting)
    mps = Transform.change_column_order(mps)
    return mps
