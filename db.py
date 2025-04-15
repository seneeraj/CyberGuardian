
import sqlite3
from datetime import datetime

def connect_db():
    return sqlite3.connect("cyber_guardian.db", check_same_thread=False)

def create_table():
    conn = connect_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS phishing_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        verdict TEXT,
        reason TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def log_url_check(url, verdict, reason):
    conn = connect_db()
    conn.execute("INSERT INTO phishing_logs (url, verdict, reason) VALUES (?, ?, ?)", (url, verdict, reason))
    conn.commit()
    conn.close()

def get_recent_logs(limit=10):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT url, verdict, reason, timestamp FROM phishing_logs ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows
