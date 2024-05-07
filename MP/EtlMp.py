import pandas as pd
import MP.extract.MpExtractor as Extract
import MP.transform.MpTransformer as Transform


def prepare_mp() -> pd.DataFrame:
    mp = Extract.get_mps()
    mp = Transform.drop_unused_columns(mp)
    mp = Transform.change_column_order(mp)
    return mp
