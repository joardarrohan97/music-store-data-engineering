import logging

from sqlalchemy import text

from extract import extract_customers, get_database_engine
from transform import transform_customers


# ==========================================
# LOGGING CONFIGURATION
# ==========================================

logging.basicConfig(
    filename="../Documentation/logs/etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ==========================================
# LOAD
# ==========================================

def load_customers(df):
    """Load transformed customer data into PostgreSQL."""

    logger.info("Starting load step")

    engine = get_database_engine()

    df.to_sql(
        "customer_clean",
        engine,
        schema="public",
        if_exists="replace",
        index=False
    )

    logger.info(
        f"Loaded {len(df)} rows into customer_clean"
    )

    print("✅ Data loaded successfully!")
    print("Target table: customer_clean")

    # Validate the load
    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT COUNT(*) FROM customer_clean")
        )

        loaded_rows = result.scalar()

    engine.dispose()

    if loaded_rows != len(df):
        raise ValueError(
            f"Validation failed: expected {len(df)} rows, "
            f"but found {loaded_rows}"
        )

    logger.info(
        f"Validation successful: {loaded_rows} rows"
    )

    print("✅ Validation successful!")
    print(f"Rows in customer_clean: {loaded_rows}")

    return loaded_rows


# ==========================================
# COMPLETE ETL PIPELINE
# ==========================================

def run_pipeline():
    """Run the complete ETL pipeline."""

    logger.info("========== ETL PIPELINE STARTED ==========")

    print("\n========== ETL PIPELINE STARTED ==========\n")

    try:

        # Extract
        logger.info("Starting extraction")
        df = extract_customers()

        # Transform
        logger.info("Starting transformation")
        df = transform_customers(df)

        # Load
        logger.info("Starting load")
        load_customers(df)

        logger.info("========== ETL PIPELINE COMPLETED ==========")

        print("\n========== ETL PIPELINE COMPLETED ==========\n")

    except Exception as error:

        logger.exception(
            f"ETL pipeline failed: {error}"
        )

        print("\n❌ ETL PIPELINE FAILED")
        print(f"Error: {error}")

        raise


# ==========================================
# ENTRY POINT
# ==========================================

if __name__ == "__main__":
    run_pipeline()