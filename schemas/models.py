from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from datetime import date

Base = declarative_base()

class people_base(BaseModel):
    name : str
    positions : str
    about : str
    address : str
    phone_01 : str
    phone_02 : Optional[str]
    mail : str
    linkedin : Optional[str]

class people_out(people_base):
    id: int
    name : str
    positions : str
    about : str
    address : str
    phone_01 : str
    phone_02 : Optional[str]
    mail : str
    linkedin : Optional[str]
    class Config:
        orm_mode = True

class people_out_id(people_base):
    id: int
    class Config:
        orm_mode = True

class academic_training_base(BaseModel):
    name : str
    institution : str
    level : str
    address : str
    start_date : date
    end_date : date
    about : str
    
class academic_training__out(academic_training_base):
    id: int
    name : str
    institution : str
    level : str
    address : str
    start_date : date
    end_date : date
    about : str
    class Config:
        orm_mode = True


class extracurricular_courses_base(BaseModel):
    name : str
    institution : str
    level : str
    address : str
    hours : int
    about : str
    
class extracurricular_courses_out(extracurricular_courses_base):
    id: int
    name : str
    institution : str
    level : str
    address : str
    hours : int
    about : str
    class Config:
        orm_mode = True


class experience_base(BaseModel):
    name : str
    enterprise : str
    position : str
    address : str
    start_date : date
    end_date : date
    about : str
    
class experience_out(experience_base):
    id: int
    name : str
    enterprise : str
    position : str
    address : str
    start_date : date
    end_date : date
    about : str
    class Config:
        orm_mode = True

    
class projects_base(BaseModel):
    name : str
    tags : str
    resume : str
    about : str
    start_date : date
    end_date : date
    github : date

class projects_out(projects_base):
    id: int
    name : str
    tags : str
    resume : str
    about : str
    start_date : date
    end_date : date
    github : date
    class Config:
        orm_mode = True
    
class technical_skills_base(BaseModel):
    name : str
    level : str
    percent_level : int
    
class technical_skills_out(technical_skills_base):
    id: int
    name : str
    level : str
    percent_level : int
    class Config:
        orm_mode = True

class languages_base(BaseModel):
    name : str
    level : str
    
    
class languages_out(languages_base):
    id: int
    name : str
    level : str
    class Config:
        orm_mode = True
