from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password=" ",  
    database="qc_task"
)
cursor = db.cursor()

# Create the qc_persons table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS qc_persons (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        status VARCHAR(255),
        login_time TIMESTAMP NULL DEFAULT NULL  # Add login_time column
    )
""")
db.commit()

# Ensure the login_time column exists
cursor.execute("SHOW COLUMNS FROM qc_persons LIKE 'login_time'")
result = cursor.fetchone()
if not result:
    cursor.execute("""
        ALTER TABLE qc_persons
        ADD COLUMN login_time TIMESTAMP NULL DEFAULT NULL
    """)
    db.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({"error": "Invalid input"}), 400
        
        username = data.get('username')
        password = data.get('password')
        
        # Here  validate the username and password
        
        login_time = datetime.now()  # Get current datetime

        try:
            cursor.execute("""
                INSERT INTO qc_persons (username, status, login_time)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE status=%s, login_time=%s
            """, (username, "logged_in", login_time, "logged_in", login_time))
            db.commit()
            return jsonify({"message": "Logged in successfully"})
        except Exception as e:
            db.rollback()
            return jsonify({"error": str(e)}), 500
    else:
        return "Login Page"

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        data = request.json
        if not data or not data.get('username'):
            return jsonify({"error": "Invalid input"}), 400

        username = data.get('username')

        try:
            cursor.execute("UPDATE qc_persons SET status=%s WHERE username=%s", ("logged_out", username))
            db.commit()
            return jsonify({"message": "Logged out successfully"})
        except Exception as e:
            db.rollback()
            return jsonify({"error": str(e)}), 500
    else:
        return "Logout Page"

if __name__ == '__main__':
    app.run(debug=True)
