class BookingAgent:
    def __init__(self, doctor_schedule_api):
        self.api = doctor_schedule_api

    def book(self, patient_name: str, doctor_type: str):
        return f"✅ Appointment booked for {patient_name} with {doctor_type} at 10 AM tomorrow."