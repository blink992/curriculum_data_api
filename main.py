from typing import List

from fastapi import Query
from api import *
from database import *
from models.models import *
from schemas.models import *

@app.get("/")
def root():
    return {"mensagem": "API no ar!"}

@app.get("/pt/about_me", response_model=people_out)
def get_about_me_pt(people_id: int = 0, db: Session = Depends(get_db)):
    return db.query(people).filter(people.id == people_id).first()

@app.get("/pt/get_people_id", response_model=people_out_id)
def get_people_id(people_name: str, db: Session = Depends(get_db)):
    return db.query(people).filter(people.name == people_name).first()

@app.get("/pt/academic_trainig", response_model=academic_training_out)
def get_academic_training(people_id: int, db: Session = Depends(get_db)):
    return db.query(people).filter(people.id == people_id).first()

