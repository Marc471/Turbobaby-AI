# memory.py
import sqlite3
from datetime import datetime

class Memory:
    def __init__(self):
        self.conn = sqlite3.connect('memory.db')
        self._init_db()

    def _init_db(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS episodes
                            (id INTEGER PRIMARY KEY,
                             timestamp TEXT,
                             user_text TEXT,
                             ai_text TEXT)''')
        
    def log(self, user_msg, ai_msg):
        self.conn.execute("INSERT INTO episodes VALUES (NULL, ?, ?, ?)",
                        (datetime.now().isoformat(), user_msg, ai_msg))
        self.conn.commit()
