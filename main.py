from typing import List

from fastapi import Query
from api import *
from database import *
from models.models import *
from schemas.models import *

@app.get("/")
async def get_root():
    return {"mensagem": "curriculum_data_api no ar!"}

@app.head("/", status_code=status.HTTP_200_OK)
async def head_root():
    return None

@app.get("/get", response_model = people_full_out)
async def get_people_full(people_id: int = 1, db: Session = Depends(get_db)):
    person = db.query(people).filter(people.id == people_id)\
    .options(
        joinedload(people.academic_trainings),
        joinedload(people.courses),
        joinedload(people.experiences),
        joinedload(people.projects_rel),
        joinedload(people.skills),
        joinedload(people.langs)
    ).first()
    return person


@app.get("/get/people", response_model=people_out)
async def get_people(people_id: int = 1, db: Session = Depends(get_db)):
    return db.query(people).filter(people.id == people_id).first()

@app.get("/get/people_id", response_model=people_out_id)
async def get_people_id(people_name: str, db: Session = Depends(get_db)):
    return db.query(people).filter(people.name == people_name).first()

@app.get("/get/academic_training", response_model=List[academic_training_out])
async def get_academic_training(people_id: int, db: Session = Depends(get_db)):
    return db.query(academic_training).filter(academic_training.people_id == people_id).all()

@app.get("/get/extracurricular_courses", response_model=List[extracurricular_courses_out])
async def get_extracurricular_courses(people_id: int, db: Session = Depends(get_db)):
    return db.query(extracurricular_courses).filter(extracurricular_courses.people_id == people_id).all()

@app.get("/get/experience", response_model=List[experience_out])
async def get_experience(people_id: int, db: Session = Depends(get_db)):
    return db.query(experience).filter(experience.people_id == people_id).all()

@app.get("/get/projects", response_model=List[projects_out])
async def get_projects(people_id: int, db: Session = Depends(get_db)):
    return db.query(projects).filter(projects.people_id == people_id).all()


@app.get("/get/technical_skills", response_model=List[technical_skills_out])
async def get_technical_skills(people_id: int, db: Session = Depends(get_db)):
    return db.query(technical_skills).filter(technical_skills.people_id == people_id).all()