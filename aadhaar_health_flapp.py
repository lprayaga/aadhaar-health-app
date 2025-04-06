
# ✅ Aadhaar-Linked Health App with Federated Learning Prediction Panel

import streamlit as st
import json
import os
import numpy as np
import joblib
from datetime import datetime

# ------------------ Data & Model ------------------
PATIENT_DB = "patients_data.json"
MODEL_PATH = "fl_model.pkl"

if os.path.exists(PATIENT_DB):
    with open(PATIENT_DB, "r") as f:
        patient_data = json.load(f)
else:
    patient_data = {}

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

# ------------------ App Layout ------------------
st.set_page_config(page_title="Aadhaar Health App", layout="wide")
st.title("🩺 Aadhaar-Linked Health Card Portal")

col1, col2 = st.columns([1, 3])

with col1:
    st.header("Patient Login")
    aadhaar_input = st.text_input("Enter Aadhaar Number")
    otp = st.text_input("Enter OTP sent to your mobile", type="password")
    authenticated = False

    if aadhaar_input in patient_data and otp == "1234":
        st.success(f"Welcome {patient_data[aadhaar_input]['name']}")
        st.success("✅ Authentication successful!")
        authenticated = True
    elif otp:
        st.error("Authentication failed. Try again.")

with col2:
    if authenticated:
        st.subheader("📋 Medical Records")
        records = patient_data[aadhaar_input].get("records", [])
        for record in sorted(records, key=lambda r: r['date'], reverse=True):
            st.markdown(f"**{record['date']}** | *{record['diagnosis']}* | 💊 {record['prescription']}")

        # Add new record
        with st.expander("➕ Add New Visit Record"):
            with st.form("add_record_form"):
                visit_date = st.date_input("Visit Date", datetime.today())
                diagnosis = st.text_input("Diagnosis")
                prescription = st.text_input("Prescription")
                submitted = st.form_submit_button("Add Record")
                if submitted:
                    new_record = {
                        "date": str(visit_date),
                        "diagnosis": diagnosis,
                        "prescription": prescription
                    }
                    patient_data[aadhaar_input].setdefault("records", []).append(new_record)
                    with open(PATIENT_DB, "w") as f:
                        json.dump(patient_data, f, indent=2)
                    st.success("✅ Record added successfully!")

        # Doctor-only section
        with st.expander("👨‍⚕️ Doctor Login (Required to Add Records)"):
            if st.checkbox("Doctor Access Panel"):
                st.subheader("🤖 Predict Patient Risk (FL Model)")
                if model is None:
                    st.warning("Federated model not found.")
                else:
                    with st.form("predict_form"):
                        age = st.number_input("Age", 18, 100)
                        bp = st.number_input("Blood Pressure")
                        sugar = st.number_input("Sugar Level")
                        med_count = st.number_input("Medication Count")
                        prev_visits = st.number_input("Previous Visits")
                        pred_submit = st.form_submit_button("Predict Risk")
                        if pred_submit:
                            features = np.array([[age, bp, sugar, med_count, prev_visits]])
                            risk_score = model.predict_proba(features)[0][1]
                            st.success(f"Predicted Risk Level: {risk_score:.2%}")
    else:
        st.info("Please authenticate using Aadhaar and OTP to view medical records.")

st.markdown("""
---
*Mock App for Aadhaar-Linked Health Card + Federated Learning Demo Only*
""")
