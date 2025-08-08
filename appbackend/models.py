from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from appbackend.database import Base  #Base database.py

class Medecin(Base):
    __tablename__ = "medecins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    doctorid = Column(Integer, ForeignKey("medecins.id"))
    name = Column(String)
    age = Column(Integer)
    sex = Column(String)
    glucose = Column(Float)
    bmi = Column(Float)
    bloodpressure = Column(Float)
    pedigree = Column(Float)
    result = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    patientid = Column(Integer, ForeignKey("patients.id"))
    result = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

