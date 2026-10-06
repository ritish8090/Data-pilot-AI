import os
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DB_USER = quote_plus(os.getenv("DB_USER"))
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print(DATABASE_URL)   # Temporary

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


def run_query(query: str) -> pd.DataFrame:
    """
    Execute a SELECT query and return a DataFrame.
    """

    with engine.connect() as conn:
        df = pd.read_sql_query(
            text(query),
            conn
        )

    return df


def execute_sql(query: str):
    """
    Execute INSERT, UPDATE, DELETE, CREATE, DROP etc.
    """

    with engine.begin() as conn:
        conn.execute(text(query))