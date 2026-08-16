import pandas as pd
from sqlalchemy import create_engine

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


def get_database_engine():
    """Create and return a PostgreSQL SQLAlchemy engine."""

    database_url = (
        f"postgresql+psycopg://"
        f"{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return create_engine(database_url)


def extract_customers():
    """Extract customer data from PostgreSQL."""

    engine = get_database_engine()

    query = """
        SELECT *
        FROM customer;
    """

    df = pd.read_sql(query, engine)

    engine.dispose()

    print("✅ Data extracted")
    print(f"Rows extracted: {len(df)}")

    return df


if __name__ == "__main__":
    extract_customers()