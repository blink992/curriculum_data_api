from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from datetime import date

Base = declarative_base()

class peopleBase(BaseModel):
    name : str
    positions : str
    about : str
    address : str
    phone_01 : str
    phone_02 : Optional[str]
    mail : str
    linkedin : Optional[str]

class peopleOut(peopleBase):
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


class academic_trainingBase(BaseModel):
    name : str
    institution : str
    level : str
    address : str
    start_date : date
    end_date : date
    about : str
    
class academic_trainingOut(academic_trainingBase):
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


class extracurricular_coursesBase(BaseModel):
    name : str
    institution : str
    level : str
    address : str
    hours : int
    about : str
    
class extracurricular_coursesOut(extracurricular_coursesBase):
    id: int
    name : str
    institution : str
    level : str
    address : str
    hours : int
    about : str
    class Config:
        orm_mode = True


class experienceBase(BaseModel):
    name : str
    enterprise : str
    position : str
    address : str
    start_date : date
    end_date : date
    about : str
    
class experienceOut(experienceBase):
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

    
class projectsBase(BaseModel):
    name : str
    tags : str
    resume : str
    about : str
    start_date : date
    end_date : date
    github : date

class projectsOut(projectsBase):
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
    
class technical_skillsBase(BaseModel):
    name : str
    level : str
    percent_level : int
    
class technical_skillsOut(technical_skillsBase):
    id: int
    name : str
    level : str
    percent_level : int
    class Config:
        orm_mode = True

class languagesBase(BaseModel):
    name : str
    level : str
    
    
class languagesOut(languagesBase):
    id: int
    name : str
    level : str
    class Config:
        orm_mode = True
