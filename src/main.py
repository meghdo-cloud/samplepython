from flask import Flask, request, jsonify
from database import get_db_connection

app = Flask(__name__)

@app.route('/isActive', methods=['GET'])
def is_active():
    return jsonify({"message": "Welcome to Drizzle"})

@app.route('/data', methods=['POST'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)