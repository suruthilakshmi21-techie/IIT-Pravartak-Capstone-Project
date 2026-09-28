from src.db.patient_db import PatientDB

class HistoryAgent:
    def __init__(self, db_path="patients.db"):
        self.db = PatientDB(db_path)

    def retrieve_history(self, patient_name: str):
        return self.db.get_history(patient_name)

    def add_history(self, name: str, age: int, condition: str, history: str):
        self.db.add_patient(name, age, condition, history)
        return f"History added for {name}."