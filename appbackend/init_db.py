# init_db.py

from database import engine, Base
import models

print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Tables créées avec succès.")
