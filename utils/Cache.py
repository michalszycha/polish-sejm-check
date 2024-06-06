import os
import pandas as pd


def cache_value(file: str, prefix: str, operation, *args, purge: bool = True):
    if not os.path.exists("./cache"):
        os.makedirs("./cache")

    file_path = f"./cache/{file}_{prefix}.csv"

    if os.path.exists(file_path) and not purge:
        return pd.read_csv(file_path)

    if not callable(operation):
        return None

    result = operation(*args)

    result.to_csv(file_path, sep=',', index=False)

    return result
