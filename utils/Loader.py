import pandas as pd
from sqlalchemy import create_engine, inspect, text


def load_to_sql(df: pd.DataFrame, name: str):
    engine = create_engine(f"sqlite:///{name}.db")
    inspector = inspect(engine)
    connection = engine.connect()

    if inspector.has_table(name):
        connection.execute(text(f"DROP TABLE {name}"))

    df.to_sql(name, engine, index=False)

    connection.close()


def load_to_csv(df: pd.DataFrame, name: str):
    df.to_csv(f"{name}.csv", sep=',')
