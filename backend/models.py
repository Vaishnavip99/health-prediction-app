# models.py
from sqlalchemy import Column, Integer, String, Date, Float
from backend.database import Base

class Patient(Base):
    __tablename__ = "patients"
   
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    dob = Column(Date, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    glucose = Column(Float, nullable=False)
    haemoglobin = Column(Float, nullable=False)
    cholesterol = Column(Float, nullable=False)
    remarks = Column(String(50))

