from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from datetime import date

Base = declarative_base()
class academic_training_base(BaseModel):
    people_id : int
    name : str
    institution : str
    level : str
    address : str
    start_date : date
    end_date : Optional[date]
    about : str
    
    
class academic_training_out(academic_training_base):
    id: int
    class Config:
        from_attributes = True


class extracurricular_courses_base(BaseModel):
    people_id : int
    name : str
    institution : str
    level : str
    address : str
    start_date : date
    end_date : Optional[date]
    hours : int
    about : str
    
class extracurricular_courses_out(extracurricular_courses_base):
    id: int
    class Config:
        from_attributes = True


class experience_base(BaseModel):
    people_id : int
    name : str
    enterprise : str
    position : str
    address : str
    start_date : date
    end_date : Optional[date]
    about : str
    
class experience_out(experience_base):
    id: int
    class Config:
        from_attributes = True

    
class projects_base(BaseModel):
    people_id : int
    name : str
    tags : str
    resume : str
    about : str
    start_date : date
    end_date : Optional[date]
    github : Optional[str]
    importance : int

class projects_out(projects_base):
    id: int
    class Config:
        from_attributes = True
    
class technical_skills_base(BaseModel):
    people_id : int
    name : str
    level : str
    percent_level : int
    about : str
    
class technical_skills_out(technical_skills_base):
    id: int
    class Config:
        from_attributes = True

class languages_base(BaseModel):
    people_id : int
    name : str
    level : str
    
class languages_out(languages_base):
    id: int
    class Config:
        from_attributes = True

class people_base(BaseModel):
    username: str
    name : str
    positions : str
    about : str
    address : str
    phone_01 : str
    phone_02 : Optional[str]
    mail : str
    linkedin : Optional[str]
    password : str
    token: Optional[str]

class people_out(people_base):
    id: int
    class Config:
        from_attributes = True

class people_full_out(people_base):
    id: int

    academic_trainings: List[academic_training_out] = []
    courses: List[extracurricular_courses_out] = []
    experiences: List[experience_out] = []
    projects_rel: List[projects_out] = [] 
    skills: List[technical_skills_out] = []
    langs: List[languages_out] = []
    class Config:
        from_attributes = True

class people_full_in(people_base):
    academic_trainings: List[academic_training_base] 
    courses: List[extracurricular_courses_base]
    experiences: List[experience_base]
    projects_rel: List[projects_base] 
    skills: List[technical_skills_base] 
    langs: List[languages_base]
    
class people_out_username(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class user_login(BaseModel):
    username: str
    password: str
    
class token(BaseModel):
    token: str
    