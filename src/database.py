import os
import psycopg2
import logging

logger = logging.getLogger(__name__)

def get_db_connection():
   logger.info(f"Attempting database connection to {os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')} as {os.environ.get('DB_USER')}")
    try:
        # Check if environment variables are set
        required_vars = ['DB_NAME', 'DB_USER', 'DB_PASSWORD']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            raise Exception(f"Missing required environment variables: {', '.join(missing_vars)}")
            
        logger.info("Connection parameters validated, connecting...")
        connection = psycopg2.connect(
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            sslmode='require'
            )
         logger.info("Connection successful")
        return connection
    except Exception as e:
        logger.error(f"Database connection error: {str(e)}", exc_info=True)
        raise
