import pandas as pd
from sqlalchemy import create_engine, inspect, text


def load_mps_to_sql(mps: pd.DataFrame):
    engine = create_engine("sqlite:///mps.db")
    inspector = inspect(engine)
    connection = engine.connect()

    if inspector.has_table("mps"):
        connection.execute(text("DROP TABLE mps"))

    mps.to_sql("mps", engine, index=False)

    connection.close()


def load_mp_to_csv(mps: pd.DataFrame):
    mps.to_csv("mps.csv", sep=',')
