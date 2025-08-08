from sqlalchemy.orm import Session
from datetime import datetime
from appbackend.models import Patient

def create_patient(db: Session, doctor_id: int, name: str, age: int, sex: str,
                   glucose: float, bmi: float, bloodpressure: float,
                   pedigree: float, result: int):
    patient = Patient(
        doctorid=doctor_id,
        name=name,
        age=age,
        sex=sex,
        glucose=glucose,
        bmi=bmi,
        bloodpressure=bloodpressure,
        pedigree=pedigree,
        result=result,
        created_at=datetime.utcnow()
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def get_patient(db: Session, patient_id: int, doctor_id: int = None):
    query = db.query(Patient).filter(Patient.id == patient_id)
    if doctor_id:
        query = query.filter(Patient.doctorid == doctor_id)
    return query.first()

def get_patients_by_doctor(db: Session, doctor_id: int):
    return db.query(Patient).filter(Patient.doctorid == doctor_id).all()

def get_all_patients(db: Session):
    return db.query(Patient).all()

def update_patient(db: Session, patient_id: int, doctor_id: int, data: dict):
    patient = get_patient(db, patient_id, doctor_id)
    if not patient:
        return None
    for key, value in data.items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

def delete_patient(db: Session, patient_id: int, doctor_id: int):
    patient = get_patient(db, patient_id, doctor_id)
    if not patient:
        return None
    db.delete(patient)
    db.commit()
    return patient
