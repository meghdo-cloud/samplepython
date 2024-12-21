from flask import Flask, request, jsonify
from database import get_db_connection

app = Flask(__name__)

# Add URL prefix for all routes
URL_PREFIX = '/drizzle-python'

@app.route(f'{URL_PREFIX}/health/live', methods=['GET'])
def liveness():
    return jsonify({"status": "ok"}), 200

@app.route(f'{URL_PREFIX}/health/ready', methods=['GET'])
def readiness():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

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
        return jsonify({"error": str(e)}), 500