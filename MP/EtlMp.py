import pandas as pd
import MP.extract.MpExtractor as Extract
import MP.transform.MpTransformer as Transform
import MP.load.MpLoader as Load


def prepare_mp() -> pd.DataFrame:
    mps = Extract.get_mps()
    mps = Transform.drop_unused_columns(mps)
    mps = Transform.change_column_order(mps)
    Load.load_mp_to_csv(mps)
    Load.load_mps_to_sql(mps)
    return mps
