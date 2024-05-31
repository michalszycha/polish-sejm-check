import pandas as pd
import sitting.extract.SittingExtractor as Extract
import sitting.transform.SittingTransform as Transform


def prepare_sittings() -> pd.DataFrame:
    sittings = Extract.get_sittings()
    sittings = Transform.transform_sittings(sittings)
    return sittings
