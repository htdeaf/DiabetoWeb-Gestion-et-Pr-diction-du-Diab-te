---

## 📄 README.md

```markdown
# 🩺 DiabetoWeb – Gestion et Prédiction du Diabète

DiabetoWeb est une application web développée avec **FastAPI**, **PostgreSQL** et un modèle de **Machine Learning** permettant aux médecins de gérer les dossiers médicaux de leurs patients et de prédire le risque de diabète.

---

## 📌 Fonctionnalités

- **Authentification sécurisée des médecins**
- **Gestion complète des patients** (ajout, modification, suppression)
- **Prédiction du diabète** via un modèle de ML pré-entraîné
- **Tableau de bord interactif** avec statistiques
- **Interface simple et intuitive** (HTML + CSS + Jinja2)

---

## 📂 Structure du projet

```

📦appbackend
┣ 📂crud                # Fonctions CRUD pour médecins et patients
┣ 📂routes              # Routes FastAPI (auth, patients)
┣ 📜config.py           # Configuration (BDD, variables d'environnement)
┣ 📜database.py         # Connexion à PostgreSQL via SQLAlchemy
┣ 📜init\_db.py          # Script d'initialisation de la base de données
┣ 📜main.py             # Point d'entrée de l'application
┣ 📜models.py           # Définition des modèles SQLAlchemy
┣ 📜schemas.py          # Schémas Pydantic pour validation
┣ 📜services.py         # Services métiers (ML, logique)

````

---

## 🚀 Installation et Exécution

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/ton-utilisateur/DiabetoWeb.git
cd DiabetoWeb/appbackend
````

### 2️⃣ Créer et activer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurer la base de données

* Installer **PostgreSQL**
* Créer une base de données (par exemple `diabetoweb`)
* Mettre à jour la variable `DATABASE_URL` dans `config.py` :

```python
DATABASE_URL = "postgresql://username:password@localhost/diabetoweb"
```

* Initialiser la BDD :

```bash
python init_db.py
```

### 5️⃣ Lancer l’application

```bash
uvicorn appbackend.main:app --reload
```

Application disponible sur : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📊 Modèle de Machine Learning

* Le modèle entraîné (`model.pkl`) doit être placé dans le dossier `appbackend`.
* Chargé automatiquement au démarrage pour effectuer les prédictions.

---

## 👩‍⚕️ Utilisation

1. Se connecter via `/login`
2. Accéder au tableau de bord `/patients`
3. Ajouter un patient et obtenir une prédiction
4. Visualiser les statistiques globales

---

## 🛠 Technologies

* **Backend** : FastAPI
* **Frontend** : HTML, CSS, Jinja2
* **Base de données** : PostgreSQL + SQLAlchemy
* **Machine Learning** : scikit-learn
* **Serveur** : Uvicorn

---




