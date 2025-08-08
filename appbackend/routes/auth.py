from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from appbackend.database import get_db
from appbackend.crud import medecin as crud_medecin
from appbackend.config import templates


router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse)
def login_post(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    medecin = crud_medecin.authenticate_medecin(db, username, password)
    if medecin:
        # Ici gérer session + redirection / dashboard
        return RedirectResponse(url="/dashboard", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Nom d'utilisateur ou mot de passe incorrect."})

@router.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register", response_class=HTMLResponse)
def register_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db)
):
    if password != confirm_password:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Les mots de passe ne correspondent pas"})

    existing_user = crud_medecin.get_medecin_by_email(db, email)
    if existing_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Un compte avec cet email existe déjà"})

    crud_medecin.create_medecin(db, username, email, password)

    return templates.TemplateResponse("login.html", {"request": request, "message": "Compte créé avec succès. Veuillez vous connecter."})
