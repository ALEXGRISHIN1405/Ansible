from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='postgres')
    return conn

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM test;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)