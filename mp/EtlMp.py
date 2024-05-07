import pandas as pd
import mp.extract.MpExtractor as Extract
import mp.transform.MpTransformer as Transform
import utils.Loader as Load


def prepare_mp() -> pd.DataFrame:
    mps = Extract.get_mps()
    mps = Transform.drop_unused_columns(mps)
    mps = Transform.change_column_order(mps)
    Load.load_to_csv(mps, "mps")
    Load.load_to_sql(mps, "mps")
    return mps
