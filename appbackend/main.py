from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from appbackend.routes import auth, patients

app = FastAPI()

app.mount("/static", StaticFiles(directory=r"C:\\Users\\Rehmi Salma\\Documents\\DiabetWeb\\static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="verysecretkey123")

templates = Jinja2Templates(directory="app/templates")

# Inclure les routeurs
app.include_router(auth.router)
app.include_router(patients.router)
