#version 2 saves the new record
import streamlit as st
import json
import os
from datetime import date

# -------------------------------
# Load or Initialize Patient Data
# -------------------------------
DATA_FILE = "patients_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        # Default hardcoded data if file doesn't exist
        return {
            "123456789012": {
                "name": "Ravi Kumar",
                "phone": "9876543210",
                "otp": "123456",
                "records": [
                    {"date": "2024-12-10", "diagnosis": "Diabetes Type 2", "prescription": "Metformin"},
                    {"date": "2025-02-14", "diagnosis": "Hypertension", "prescription": "Amlodipine"}
                ]
            },
            "987654321098": {
                "name": "Anjali Sharma",
                "phone": "9123456789",
                "otp": "654321",
                "records": [
                    {"date": "2025-01-05", "diagnosis": "Asthma", "prescription": "Inhaler"}
                ]
            }
        }

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

patients_db = load_data()

# -------------------------------
# Streamlit App
# -------------------------------
st.title("🩺 Aadhaar-Linked Health Card Portal")

st.sidebar.header("Patient Login")
aadhaar_input = st.sidebar.text_input("Enter Aadhaar Number")

if aadhaar_input in patients_db:
    st.sidebar.success(f"Welcome {patients_db[aadhaar_input]['name']}")
    otp_input = st.sidebar.text_input("Enter OTP sent to your mobile", type="password")

    if otp_input == patients_db[aadhaar_input]["otp"]:
        st.sidebar.success("✅ Authentication successful!")

        # View Medical Records
        st.subheader("📋 Medical Records")
        records = patients_db[aadhaar_input]["records"]
        for record in records:
            st.markdown(f"- **{record['date']}** | *{record['diagnosis']}* | 💊 {record['prescription']}")

        # Add New Record
        st.subheader("➕ Add New Visit Record")
        with st.form("new_visit_form"):
            visit_date = st.date_input("Visit Date", value=date.today())
            diagnosis = st.text_input("Diagnosis")
            prescription = st.text_input("Prescription")
            submitted = st.form_submit_button("Add Record")

            if submitted:
                new_entry = {
                    "date": visit_date.strftime("%Y-%m-%d"),
                    "diagnosis": diagnosis,
                    "prescription": prescription
                }
                patients_db[aadhaar_input]["records"].append(new_entry)
                save_data(patients_db)
                st.success("✅ Record added successfully! Please refresh to see updated data.")

    elif otp_input != "":
        st.sidebar.error("❌ Invalid OTP")
else:
    if aadhaar_input:
        st.sidebar.error("❌ Aadhaar number not found")

st.markdown("---")
st.caption("Mock App for Aadhaar-Linked Health Card - Demo Only")
