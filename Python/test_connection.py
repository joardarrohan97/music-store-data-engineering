import psycopg

HOST = "localhost"
PORT = 5432
DATABASE = "music_store_analysis"
USERNAME = "rohanjoardar"

try:
    with psycopg.connect(
        host=HOST,
        port=PORT,
        dbname=DATABASE,
        user=USERNAME
    ) as connection:

        print("✅ Successfully connected to PostgreSQL!")
        print(f"Database: {DATABASE}")
        print(f"Host: {HOST}")
        print(f"User: {USERNAME}")

except Exception as error:
    print("❌ Connection failed!")
    print(error)