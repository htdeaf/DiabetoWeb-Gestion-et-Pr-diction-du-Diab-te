from sqlalchemy.orm import Session
from appbackend.models import Medecin
from appbackend.config import templates

def get_medecin_by_username(db: Session, username: str):
    return db.query(Medecin).filter(Medecin.username == username).first()

def get_medecin_by_email(db: Session, email: str):
    return db.query(Medecin).filter(Medecin.email == email).first()

def authenticate_medecin(db: Session, username: str, password: str):
    return db.query(Medecin).filter(Medecin.username == username, Medecin.password == password).first()

def create_medecin(db: Session, username: str, email: str, password: str):
    new_user = Medecin(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
