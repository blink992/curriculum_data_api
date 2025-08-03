from typing import List, cast

from fastapi import Body

from api import *
from database import *
from models.models import *
from schemas.models import *

from passlib.context import CryptContext
import secrets
from sqlalchemy import and_, func

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_simple_token(length: int = 32) -> str:
    """
    Gera um token hexadecimal aleatório usando o módulo secrets.

    Args:
        length (int): O comprimento desejado do token em caracteres.

    Returns:
        str: O token hexadecimal gerado.
    """
    if length % 2 != 0:
        raise ValueError("O comprimento do token deve ser um número par para representação hexadecimal.")
    num_bytes = length // 2
    return secrets.token_bytes(num_bytes).hex()



@app.get("/")
async def get_root():
    return {"mensagem": "curriculum_data_api no ar!"}

@app.head("/", status_code=status.HTTP_200_OK)
async def head_root():
    return None

# Give academic training by id user
@app.get("/get/people", response_model=people_out)
async def get_people(people_id: int = 1, db: Session = Depends(get_db)):
    data = db.query(people).filter(people.id == people_id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Person not found")
    
    return data

# Give academic training by id user
@app.get("/get/academic_training", response_model=List[academic_training_out])
async def get_academic_training(people_id: int, db: Session = Depends(get_db)):
    data = db.query(academic_training).filter(academic_training.people_id == people_id).all()
    if data is None:
        raise HTTPException(status_code=404, detail="Academic Training not found")
    
    return data

# Give extracurricular courses by id user
@app.get("/get/extracurricular_courses", response_model=List[extracurricular_courses_out])
async def get_extracurricular_courses(people_id: int, db: Session = Depends(get_db)):
    data = db.query(extracurricular_courses).filter(extracurricular_courses.people_id == people_id).all()
    if data is None:
        raise HTTPException(status_code=404, detail="Extracurricular Course not found")

    return data

# Give experience by id user
@app.get("/get/experience", response_model=List[experience_out])
async def get_experience(people_id: int, db: Session = Depends(get_db)):
    data = db.query(experience).filter(experience.people_id == people_id).all()
    if data is None:
        raise HTTPException(status_code=404, detail="Experience not found")
    
    return data

# Give projects by id user
@app.get("/get/projects", response_model=List[projects_out])
async def get_projects(people_id: int, db: Session = Depends(get_db)):
    data = db.query(projects).filter(projects.people_id == people_id).all()
    if data is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return data

# Give technicall skills by id user
@app.get("/get/technical_skills", response_model=List[technical_skills_out])
async def get_technical_skills(people_id: int, db: Session = Depends(get_db)):
    data = db.query(technical_skills).filter(technical_skills.people_id == people_id).all()
    if data is None:
        raise HTTPException(status_code=404, detail="Technicall Skill not found")
    
    return data    

# Validate if username exists by id user
@app.get("/get/verify_username")
async def verify_user(username: str, db: Session = Depends(get_db)):
    person = db.query(people.id).filter(people.username == username.strip()).first()
    if person:
        return True
    return False

# Register a new user in the database
@app.post("/post/people")
async def post_people(person_data_in: people_full_in, db: Session = Depends(get_db)):
    
    if verify_user(person_data_in.username):
        raise HTTPException(status_code=404, detail="Technicall Skill not found")
    
    hashed_password = pwd_context.hash(person_data_in.password)
    
    person_data_dict = person_data_in.model_dump(
        exclude={
            'password', # Exclui a senha em texto puro
            'academic_trainings', 
            'courses', 
            'experiences', 
            'projects_rel', 
            'skills', 
            'langs'
        }
    )
    
    person_data_dict['password'] = hashed_password
    
    db_person = people(**person_data_dict)

    db.add(db_person)
    db.flush() 
    
    if person_data_in.academic_trainings:
        for item_data in person_data_in.academic_trainings:
            db_person.academic_trainings.append(academic_training(**item_data.model_dump()))

    if person_data_in.courses:
        for item_data in person_data_in.courses:
            db_person.courses.append(extracurricular_courses(**item_data.model_dump()))

    if person_data_in.experiences:
        for item_data in person_data_in.experiences:
            db_person.experiences.append(experience(**item_data.model_dump()))

    if person_data_in.projects_rel:
        for item_data in person_data_in.projects_rel:
            db_person.projects_rel.append(projects(**item_data.model_dump()))

    if person_data_in.skills:
        for item_data in person_data_in.skills:
            db_person.skills.append(technical_skills(**item_data.model_dump()))

    if person_data_in.langs:
        for item_data in person_data_in.langs:
            db_person.langs.append(languages(**item_data.model_dump()))

    db.commit()
    db.refresh(db_person)

    return "Usuário cadastrado com sucesso!"

# Receive token and validate this, if truthy give all curriculum data of user
@app.post("/post/curriculum_by_token")
async def curriculum_by_token(token: str = Body(..., embed=True), db: Session = Depends(get_db)):
    data = db.query(people).filter(people.token == token)\
    .options(
        joinedload(people.academic_trainings),
        joinedload(people.courses),
        joinedload(people.experiences),
        joinedload(people.projects_rel),
        joinedload(people.skills),
        joinedload(people.langs)
    ).first()
    
    if data is None:
        raise HTTPException(status_code=404, detail="Invalid token")
    else:
        return data

# Update token of the user
@app.patch("/patch/token")
async def patch_token(update_token_data: user_login, db: Session = Depends(get_db)):
    validate_login_data = await verify_pass(update_token_data.username, update_token_data.password, db)
    if validate_login_data:
        data = cast(people, db.query(people).filter(people.username == update_token_data.username).first())
        setattr(data, "token", generate_simple_token())
        db.commit()
        db.refresh(data)
        return data.token
    else:
        raise HTTPException(status_code=401, detail="Invalid password or username")

# Receive data user and validate, if truthy give all curriculum data of user
@app.post("/post/curriculum")
async def curriculum(user_data: user_login, db: Session = Depends(get_db)):
    data = db.query(people).filter(people.username == user_data.username.strip())\
    .options(
        joinedload(people.academic_trainings),
        joinedload(people.courses),
        joinedload(people.experiences),
        joinedload(people.projects_rel),
        joinedload(people.skills),
        joinedload(people.langs)
    ).first()
    
    if data is None:
        raise HTTPException(status_code=404, detail="Person not found")
    else:
        return data
     
# Receive username and password and validate, return a boolean
async def verify_pass(username: str, password: str, db: Session):
    person = db.query(people).filter(people.username == username).first()
    if person != None:
        password_hash: str = cast(str, person.password)
        print(password_hash)
        return pwd_context.verify(password, password_hash)
    return False