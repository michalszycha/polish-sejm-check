import pandas as pd
from sqlalchemy import create_engine, inspect, text


def load_mps_to_sql(mps: pd.DataFrame):
    engine = create_engine("sqlite:///deputies.db")
    inspector = inspect(engine)
    connection = engine.connect()

    if inspector.has_table("MPs"):
        connection.execute(text("DROP TABLE deputies"))

    mps.to_sql("MPs", engine, index=False)

    connection.close()


def load_mp_to_csv(mps: pd.DataFrame):
    mps.to_csv("mps.csv", sep=',')
