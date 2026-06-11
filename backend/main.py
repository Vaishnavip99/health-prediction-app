from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date

from backend.database import get_db
from backend.models import Patient
from backend.crud import get_patients, update_patient, delete_patient
from backend.ml_model import predict

# --- Schema for request validation ---
class PatientCreate(BaseModel):
    full_name: str
    dob: date
    email: str
    glucose: float
    haemoglobin: float
    cholesterol: float

app = FastAPI()

@app.post("/patients/")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    # Predict health risk
    prediction = predict([[patient.glucose, patient.haemoglobin, patient.cholesterol]])
    db_patient.remarks = prediction[0]
    db.commit()
    return db_patient

@app.get("/patients/")
def read_patients(db: Session = Depends(get_db)):
    return get_patients(db)

# --- Update Patient ---
@app.put("/patients/{patient_id}")
def update_patient_record(patient_id: int, patient: PatientCreate, db: Session = Depends(get_db)):
    return update_patient(db, patient_id, patient)

# --- Delete Patient ---
@app.delete("/patients/{patient_id}")
def delete_patient_record(patient_id: int, db: Session = Depends(get_db)):
    return delete_patient(db, patient_id)