import sqlite3

class PatientDB:
    def __init__(self, db_path="patients.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            condition TEXT,
            history TEXT
        )
        """)
        self.conn.commit()

    def add_patient(self, name, age, condition, history):
        self.conn.execute("INSERT INTO patients (name, age, condition, history) VALUES (?, ?, ?, ?)",
                          (name, age, condition, history))
        self.conn.commit()

    def get_history(self, name):
        cursor = self.conn.execute("SELECT history FROM patients WHERE name=?", (name,))
        result = cursor.fetchone()
        return result[0] if result else "No history found."