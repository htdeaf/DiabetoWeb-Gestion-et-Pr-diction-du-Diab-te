from fastapi import APIRouter, Request, Depends, Form, status
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse

from appbackend.database import get_db
from appbackend.crud import patient as crud_patient
from appbackend.config import templates
from appbackend.services import predict_diabetes

router = APIRouter()
# Tableau de bord
@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    doctor_id = 1  # Simuler un médecin connecté
    patients = crud_patient.get_patients_by_doctor(db, doctor_id)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "patients": patients
    })


#ajouté un patien
@router.get("/dashboard/add",response_class=HTMLResponse)
def add_patient_form(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("add_patient.html", {"request": request})
@router.post("/dashboard/result", response_class=HTMLResponse)
def submit_patient(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    sex: str = Form(...),
    glucose: float = Form(...),
    bmi: float = Form(...),
    bloodpressure: float = Form(...),
    pedigree: float = Form(...),
    db: Session = Depends(get_db)
):
    doctor_id = 1
    result = predict_diabetes(glucose, bmi, age, pedigree)
    patient = crud_patient.create_patient(
        db, doctor_id, name, age, sex, glucose, bmi, bloodpressure, pedigree, result
    )
    return templates.TemplateResponse("result.html", {
        "request": request,
        "name": name,
        "age": age,
        "sex": sex,
        "glucose": glucose,
        "bmi": bmi,
        "bloodpressure": bloodpressure,
        "pedigree": pedigree,
        "result": result
    })
# Liste des patients
@router.get("/list_patients", response_class=HTMLResponse)
def list_patients(request: Request, db: Session = Depends(get_db)):
    doctor_id = 1  # Simuler un médecin connecté (à remplacer par auth réelle)
    patients = crud_patient.get_patients_by_doctor(db, doctor_id)
    return templates.TemplateResponse("list_patients.html", {"request": request, "patients": patients})

# Liste des patients
@router.get("/list_patients", response_class=HTMLResponse)
def list_patients(request: Request, db: Session = Depends(get_db)):
    doctor_id = 1  # Simuler médecin connecté
    patients = crud_patient.get_patients_by_doctor(db, doctor_id)
    return templates.TemplateResponse("list_patients.html", {"request": request, "patients": patients})

# Formulaire modification patient
@router.get("/edit/{patient_id}", response_class=HTMLResponse)
def edit_patient_form(patient_id: int, request: Request, db: Session = Depends(get_db)):
    doctor_id = 1
    patient = crud_patient.get_patient(db, patient_id, doctor_id)
    if not patient:
        return RedirectResponse(url="/list_patients", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("edit_patient.html", {"request": request, "patient": patient})

# Traitement mise à jour patient
@router.post("/edit/{patient_id}")
def update_patient(
    patient_id: int,
    name: str = Form(...),
    age: int = Form(...),
    sex: str = Form(...),
    glucose: float = Form(...),
    bmi: float = Form(...),
    bloodpressure: float = Form(...),
    pedigree: float = Form(...),
    db: Session = Depends(get_db)
):
    doctor_id = 1
    data = {
        "name": name,
        "age": age,
        "sex": sex,
        "glucose": glucose,
        "bmi": bmi,
        "bloodpressure": bloodpressure,
        "pedigree": pedigree
    }
    updated_patient = crud_patient.update_patient(db, patient_id, doctor_id, data)
    if not updated_patient:
        return RedirectResponse(url=f"/edit/{patient_id}", status_code=status.HTTP_303_SEE_OTHER)

    return RedirectResponse(url="/list_patients", status_code=status.HTTP_303_SEE_OTHER)
# Supprimer un patient

@router.get("/delete/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    doctor_id = 1  # Simuler un médecin connecté
    deleted_patient = crud_patient.delete_patient(db, patient_id, doctor_id)
    return RedirectResponse(url="/list_patients", status_code=status.HTTP_303_SEE_OTHER)


# from fastapi import APIRouter, Request, Depends, Form
# from sqlalchemy.orm import Session
# from fastapi.responses import HTMLResponse, RedirectResponse

# from appbackend.database import get_db
# from appbackend.crud import patient as crud_patient
# from appbackend.config import templates
# from appbackend.services import predict_diabetes

# router = APIRouter()

# # Tableau de bord
# @router.get("/dashboard", response_class=HTMLResponse)
# def dashboard(request: Request, db: Session = Depends(get_db)):
#     patients = crud_patient.get_all_patients(db)
#     return templates.TemplateResponse("patients.html", {"request": request, "patients": patients})
# #ajouté un patien
# @router.get("/patients/add", response_class=HTMLResponse)
# def add_patient_form(request: Request):
#     return templates.TemplateResponse("add_patient.html", {"request": request})

# @router.post("/submit")
# def submit_patient(
#     request: Request,
#     name: str = Form(...),
#     age: int = Form(...),
#     sex: str = Form(...),
#     glucose: float = Form(...),
#     bmi: float = Form(...),
#     bloodpressure: float = Form(...),
#     pedigree: float = Form(...),
#     db: Session = Depends(get_db)
# ):
#     # Simuler médecin connecté
#     doctor_id = 1

#     result = predict_diabetes(glucose, bmi, age, pedigree)

#     patient = crud_patient.create_patient(db, doctor_id, name, age, sex, glucose, bmi, bloodpressure, pedigree, result)

#     return templates.TemplateResponse("result.html", {
#         "request": request,
#         "name": name,
#         "age": age,
#         "sex": sex,
#         "glucose": glucose,
#         "bmi": bmi,
#         "bloodpressure": bloodpressure,
#         "pedigree": pedigree,
#         "result": result
#     })


# # Liste des patients
# @router.get("/patients/list", response_class=HTMLResponse)
# def list_patients(request: Request, db: Session = Depends(get_db)):
#     patients = crud_patient.get_all_patients(db)
#     return templates.TemplateResponse("list_patients.html", {"request": request, "patients": patients})

# @router.get("/patients", response_class=HTMLResponse)
# def list_patients(request: Request, db: Session = Depends(get_db)):
#     doctor_id = 1  # À récupérer depuis session authentifiée
#     patients = crud_patient.get_patients_by_doctor(db, doctor_id)
#     return templates.TemplateResponse("patients.html", {"request": request, "patients": patients})

# @router.get("/delete/{id}")
# def delete_patient(id: int, request: Request, db: Session = Depends(get_db)):
#     doctor_id = 1  # à récupérer session réelle
#     crud_patient.delete_patient(db, id, doctor_id)
#     return RedirectResponse(url="/patients", status_code=303)









# # Ajouter un patient
# # @router.get("/patients/add", response_class=HTMLResponse)
# # def add_patient_form(request: Request):
# #     return templates.TemplateResponse("add_patient.html", {"request": request})

# # @router.post("/patients/add", response_class=HTMLResponse)
# # def add_patient(request: Request,
# #                 name: str = Form(...),
# #                 age: int = Form(...),
# #                 glucose: float = Form(...),
# #                 bmi: float = Form(...),
# #                 db: Session = Depends(get_db)):
# #     crud_patient.create_patient(db, name, age, glucose, bmi)
# #     return RedirectResponse(url="/patients", status_code=303)

# # # Modifier un patient
# # @router.get("/patients/edit/{patient_id}", response_class=HTMLResponse)
# # def edit_patient_form(request: Request, patient_id: int, db: Session = Depends(get_db)):
# #     patient = crud_patient.get_patient(db, patient_id)
# #     return templates.TemplateResponse("edit_patient.html", {"request": request, "patient": patient})

# # @router.post("/patients/edit/{patient_id}", response_class=HTMLResponse)
# # def edit_patient(request: Request,
# #                  patient_id: int,
# #                  name: str = Form(...),
# #                  age: int = Form(...),
# #                  glucose: float = Form(...),
# #                  bmi: float = Form(...),
# #                  db: Session = Depends(get_db)):
# #     crud_patient.update_patient(db, patient_id, name, age, glucose, bmi)
# #     return RedirectResponse(url="/patients", status_code=303)

# # # Supprimer un patient
# # @router.post("/patients/delete/{patient_id}")
# # def delete_patient(patient_id: int, db: Session = Depends(get_db)):
# #     crud_patient.delete_patient(db, patient_id)
# #     return RedirectResponse(url="/patients", status_code=303)

# # # Prédiction du risque de diabète
# # @router.get("/patients/result/{patient_id}", response_class=HTMLResponse)
# # def patient_result(request: Request, patient_id: int, db: Session = Depends(get_db)):
# #     patient = crud_patient.get_patient(db, patient_id)
# #     prediction = predict_diabetes(patient)  # appel au modèle ML
# #     return templates.TemplateResponse("result.html", {
# #         "request": request,
# #         "patient": patient,
# #         "prediction": prediction
# #     })


# from fastapi import APIRouter, Request, Depends, Form, status
# from sqlalchemy.orm import Session
# from fastapi.responses import HTMLResponse, RedirectResponse

# from appbackend.database import get_db
# from appbackend.crud import patient as crud_patient
# from appbackend.config import templates
# from appbackend.services import predict_diabetes

# router = APIRouter()

# # Dashboard - liste patients du médecin connecté (ici simulé doctor_id=1)
# @router.get("/patients", response_class=HTMLResponse)
# def patients_dashboard(request: Request, db: Session = Depends(get_db)):
#     doctor_id = 1  # TODO: récupérer depuis session réelle
#     patients = crud_patient.get_patients_by_doctor(db, doctor_id)
#     # Calcul statistique simple
#     total = len(patients)
#     diabetics = sum(p.result for p in patients)
#     percent_diabetic = (diabetics / total * 100) if total > 0 else 0
#     return templates.TemplateResponse("patients.html", {
#         "request": request,
#         "patients": patients,
#         "total": total,
#         "percent_diabetic": percent_diabetic
#     })

# # Formulaire ajout patient
# @router.get("/patients/add", response_class=HTMLResponse)
# def add_patient_form(request: Request):
#     return templates.TemplateResponse("add_patient.html", {"request": request})

# # Soumission ajout patient + prédiction ML
# @router.post("/patients/add", response_class=HTMLResponse)
# def submit_patient(
#     request: Request,
#     name: str = Form(...),
#     age: int = Form(...),
#     sex: str = Form(...),
#     glucose: float = Form(...),
#     bmi: float = Form(...),
#     bloodpressure: float = Form(...),
#     pedigree: float = Form(...),
#     db: Session = Depends(get_db)
# ):
#     doctor_id = 1  # TODO: récupérer depuis session réelle
#     result = predict_diabetes(glucose, bmi, age, pedigree)

#     patient = crud_patient.create_patient(
#         db, doctor_id, name, age, sex, glucose, bmi, bloodpressure, pedigree, result
#     )

#     return templates.TemplateResponse("result.html", {
#         "request": request,
#         "patient": patient,
#         "result": result
#     })

# # Formulaire édition patient (pré-rempli)
# @router.get("/patients/edit/{patient_id}", response_class=HTMLResponse)
# def edit_patient_form(patient_id: int, request: Request, db: Session = Depends(get_db)):
#     doctor_id = 1  # TODO: récupérer depuis session réelle
#     patient = crud_patient.get_patient(db, patient_id, doctor_id)
#     if not patient:
#         return RedirectResponse(url="/patients", status_code=status.HTTP_303_SEE_OTHER)
#     return templates.TemplateResponse("edit_patient.html", {"request": request, "patient": patient})

# # Soumission modification patient
# @router.post("/patients/edit/{patient_id}")
# async def update_patient(patient_id: int, request: Request, db: Session = Depends(get_db)):
#     doctor_id = 1  # TODO: récupérer depuis session réelle
#     form = await request.form()
#     data = {
#         "name": form.get("name"),
#         "age": int(form.get("age")),
#         "sex": form.get("sex"),
#         "glucose": float(form.get("glucose")),
#         "bmi": float(form.get("bmi")),
#         "bloodpressure": float(form.get("bloodpressure")),
#         "pedigree": float(form.get("pedigree")),
#     }
#     updated = crud_patient.update_patient(db, patient_id, doctor_id, data)
#     if not updated:
#         # patient introuvable ou non modifié
#         return RedirectResponse(url="/patients", status_code=status.HTTP_303_SEE_OTHER)
#     return RedirectResponse(url="/patients", status_code=status.HTTP_303_SEE_OTHER)

# # Suppression patient
# @router.get("/patients/delete/{patient_id}")
# def delete_patient(patient_id: int, request: Request, db: Session = Depends(get_db)):
#     doctor_id = 1  # TODO: récupérer depuis session réelle
#     crud_patient.delete_patient(db, patient_id, doctor_id)
#     return RedirectResponse(url="/patients", status_code=status.HTTP_303_SEE_OTHER)




