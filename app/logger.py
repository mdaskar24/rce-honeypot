import sqlite3
import os
from datetime import datetime

# Ensure the 'database' folder exists
os.makedirs('database', exist_ok=True)

def log_command(ip, command):
    db_path = 'database/honeypot.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the logs table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            command TEXT,
            timestamp TEXT
        )
    ''')

    # Insert the command into the logs table
    timestamp = datetime.now().isoformat()
    cursor.execute('INSERT INTO logs (ip, command, timestamp) VALUES (?, ?, ?)',
                   (ip, command, timestamp))

    conn.commit()
    conn.close()

    # Optional: Print to console for debugging
    print(f"[+] Logged from {ip}: \"{command}\" at {timestamp}")
