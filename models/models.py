from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class people(Base):
    __tablename__  = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    positions = Column(String)
    about = Column(String)
    address = Column(String)
    phone_01 = Column(String)
    phone_02 = Column(String)
    mail = Column(String)
    linkedin = Column(String)

    
class academic_training(Base):
    __tablename__  = "academic_training"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    institution = Column(String)
    level = Column(String)
    address = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    about = Column(String)

class extracurricular_courses(Base):
    __tablename__  = "extracurricular_courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    institution = Column(String)
    level = Column(String)
    address = Column(String)
    hours = Column(Integer)
    about = Column(String)

class experience(Base):
    __tablename__  = "experience"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    enterprise = Column(String)
    position = Column(String)
    address = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    about = Column(String)
    
    
class projects(Base):
    __tablename__  = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tags = Column(String)
    resume = Column(String)
    about = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    github = Column(Date)

    
class technical_skills(Base):
    __tablename__  = "technical_skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    level = Column(String)
    percent_level = Column(Integer)

class languages(Base):
    __tablename__  = "languages"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    level = Column(String)