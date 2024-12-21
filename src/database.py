import os
import psycopg2

def get_db_connection():
    # Connect via Cloud SQL Proxy
    return psycopg2.connect(
        host='127.0.0.1',  # Connect to local Cloud SQL proxy
        port=os.environ['DB_PORT'],         # Default PostgreSQL port
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
