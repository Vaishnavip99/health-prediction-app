# app.py
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("Health Prediction App")

# --- Patient Form ---
with st.form("patient_form"):
    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth")
    email = st.text_input("Email Address")
    glucose = st.number_input("Glucose")
    haemoglobin = st.number_input("Haemoglobin")
    cholesterol = st.number_input("Cholesterol")
    submitted = st.form_submit_button("Submit")

    if submitted:
        response = requests.post("http://localhost:8000/patients/", json={
            "full_name": name,
            "dob": str(dob),
            "email": email,
            "glucose": glucose,
            "haemoglobin": haemoglobin,
            "cholesterol": cholesterol
        })
        st.success("Patient record added!")


# --- Fetch Patients from Backend ---
patients = requests.get("http://localhost:8000/patients/").json()

# --- Display Table ---
st.write("Patient Records")
st.table(patients)

# --- Risk Distribution Pie Chart ---
st.write("Risk Distribution")
df = pd.DataFrame(patients)
if not df.empty and "remarks" in df.columns:
    fig, ax = plt.subplots()
    df['remarks'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)
else:
    st.info("No patient data yet to visualize.")
