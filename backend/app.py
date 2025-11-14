from flask import Flask, request, jsonify
import pymysql
import os
from dotenv import load_dotenv
import jwt
import datetime

load_dotenv()

app = Flask(__name__)

# MySQL Configuration
db = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    db=os.getenv("MYSQL_DB"),
    cursorclass=pymysql.cursors.DictCursor
)

# Secret key for JWT
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()

    if user:
        token = jwt.encode({
            'user': user['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
