from flask import Flask, request, jsonify
from database import get_db_connection
import os
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

URL_PREFIX = os.getenv('URL_PREFIX', '/drizzlepython')
logger.info(f"Using URL_PREFIX: {URL_PREFIX}")

@app.route(f'{URL_PREFIX}/health/live', methods=['GET'])
def liveness():
    return jsonify({"status": "ok"}), 200

@app.route(f'{URL_PREFIX}/health/ready', methods=['GET'])
def readiness():
    try:
        logger.info("Checking database connection...")
        # Log environment variables (excluding sensitive data)
        logger.info(f"Database Host: 127.0.0.1")
        logger.info(f"Database Port: 5432")
        logger.info(f"Database Name: {str(bool(get_db_connection))}")
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        logger.info("Database connection successful")
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        # Return 503 Service Unavailable instead of 500 for readiness probe
        return jsonify({"status": "error", "message": "Database connection failed"}), 503

@app.route(f'{URL_PREFIX}/isActive', methods=['GET'])
def is_active():
    return jsonify({"message": "Welcome to Drizzle"})

@app.route(f'{URL_PREFIX}/data', methods=['POST'])
def add_data():
    try:
        data = request.json
        id = data.get('id')
        name = data.get('name')

        if not id or not name:
            return jsonify({"error": "Both id and name are required"}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(
            "INSERT INTO tablea (id, name) VALUES (%s, %s)",
            (id, name)
        )
        
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Data inserted successfully"}), 201

    except Exception as e:
        logger.error(f"Error in add_data: {str(e)}")
        return jsonify({"error": str(e)}), 500
