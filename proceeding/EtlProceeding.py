import pandas as pd
import proceeding.extract.ProceedingExtractor as Extract
import proceeding.transform.ProceedingTransform as Transform
import utils.Loader as Load


def prepare_proceedings() -> pd.DataFrame:
    proceedings = Extract.get_proceedings()
    proceedings = Transform.transform_proceedings(proceedings)
    return proceedings
