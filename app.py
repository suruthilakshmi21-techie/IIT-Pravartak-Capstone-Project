import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.agents.planner import Planner
from src.agents.booking_agent import BookingAgent
from src.agents.history_agent import HistoryAgent
from src.agents.disease_agent import DiseaseAgent

planner = Planner()
booking_agent = BookingAgent("DoctorScheduleAPI")
history_agent = HistoryAgent()
disease_agent = DiseaseAgent()

st.title("🩺 Agentic Healthcare Assistant Demo")

query = st.text_input("Enter your request:")

if query:
    tasks = planner.decompose(query)
    for task in tasks:
        if task["task"] == "book_appointment":
            st.write(booking_agent.book("Father", "Nephrologist"))
        elif task["task"] == "retrieve_history":
            st.write(history_agent.retrieve_history("Father"))
        elif task["task"] == "search_disease_info":
            st.write(disease_agent.get_latest_info("Chronic Kidney Disease"))
        else:
            st.write("Sorry, I couldn't understand the request.")