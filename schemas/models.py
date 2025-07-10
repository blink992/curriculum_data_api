from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class peopleBase(BaseModel):
    name : str
    positions : str
    about : str
    address : str
    phone_01 : str
    phone_02 : str
    mail : str
    linkedin : str

class peopleOut(peopleBase):
    id: int
    name : str
    positions : str
    about : str
    address : str
    phone_01 : str
    phone_02 : str
    mail : str
    linkedin : str
    class Config:
        orm_mode = True

# class academic_trainingBase(Base):
#     __tablename__  = "academic_training"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     institution = Column(String)
#     level = Column(String)
#     address = Column(String)
#     start_date = Column(Date)
#     end_date = Column(Date)
#     about = Column(String)

# class extracurricular_coursesBase(Base):
#     __tablename__  = "extracurricular_courses"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     institution = Column(String)
#     level = Column(String)
#     address = Column(String)
#     hours = Column(Integer)
#     about = Column(String)

# class experienceBase(Base):
#     __tablename__  = "experience"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     enterprise = Column(String)
#     position = Column(String)
#     address = Column(String)
#     start_date = Column(Date)
#     end_date = Column(Date)
#     about = Column(String)
    
    
# class projectsBase(Base):
#     __tablename__  = "projects"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     tags = Column(String)
#     resume = Column(String)
#     about = Column(String)
#     start_date = Column(Date)
#     end_date = Column(Date)
#     github = Column(Date)

    
# class technical_skillsBase(Base):
#     __tablename__  = "technical_skills"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     level = Column(String)
#     percent_level = Column(Integer)

# class languagesBase(Base):
#     __tablename__  = "languages"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     level = Column(String)