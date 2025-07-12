from typing import List

from fastapi import Query
from api import *
from database import *
from models.models import *
from schemas.models import *

@app.get("/")
async def root():
    return {"mensagem": "curriculum_data_api no ar!"}

@app.get("/health")
async def health_status():
    return {"mensagem": "curriculum_data_api no ar!"}


@app.get("/get/about_me", response_model=people_out)
async def get_about_me_pt(people_id: int = 1, db: Session = Depends(get_db)):
    return db.query(people).filter(people.id == people_id).first()

@app.get("/get/people_id", response_model=people_out_id)
async def get_people_id(people_name: str, db: Session = Depends(get_db)):
    return db.query(people).filter(people.name == people_name).first()

@app.get("/get/academic_training", response_model=List[academic_training_out])
async def get_academic_training(people_id: int, db: Session = Depends(get_db)):
    return db.query(academic_training).filter(academic_training.people_id == people_id).all()
