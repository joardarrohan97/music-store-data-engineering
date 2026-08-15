import pandas as pd


def transform_customers(df):
    """Clean and transform customer data."""

    text_columns = df.select_dtypes(
        include=["object", "str"]
    ).columns

    # Remove leading and trailing spaces
    for column in text_columns:
        df[column] = df[column].str.strip()

    # Convert email addresses to lowercase
    if "email" in df.columns:
        df["email"] = df["email"].str.lower()

    # Remove duplicate records
    df = df.drop_duplicates()

    print("✅ Data transformed")
    print(f"Rows after transformation: {len(df)}")

    return df


if __name__ == "__main__":
    print("⚠️ transform.py is designed to be called by the ETL pipeline.")