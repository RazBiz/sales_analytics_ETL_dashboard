import logging
from sqlalchemy import create_engine

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_db_engine(db_url):
    try:
        engine = create_engine(db_url)
        logging.info("Successfully connected to database.")
        return engine
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        raise