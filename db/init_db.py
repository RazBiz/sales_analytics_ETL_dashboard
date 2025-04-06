import sys

import psycopg2


def initialize_database(db_url, schema_path="db/schema.sql"):
    try:
        with psycopg2.connect(db_url) as conn:
            with conn.cursor() as cursor:
                with open(schema_path, 'r') as f:
                    cursor.execute(f.read())
                conn.commit()
        print("✅ Database initialized successfully.")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")

if __name__ == "__main__":
    import os
    db_url = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5433/retaildb")
    initialize_database(db_url)