from tkinter import CASCADE
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class people(Base):
    __tablename__  = "people"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    name = Column(String)
    positions = Column(String)
    about = Column(String)
    address = Column(String)
    phone_01 = Column(String)
    phone_02 = Column(String)
    mail = Column(String)
    linkedin = Column(String)
    password = Column(String)
    token = Column(String)
    
    academic_trainings = relationship("academic_training", back_populates="person")
    courses = relationship("extracurricular_courses", back_populates="person")
    experiences = relationship("experience", back_populates="person")
    projects_rel = relationship("projects", back_populates="person")
    skills = relationship("technical_skills", back_populates="person")
    langs = relationship("languages", back_populates="person")

    
class academic_training(Base):
    __tablename__  = "academic_training"
    id = Column(Integer, primary_key=True, index=True)
    people_id = Column(Integer, ForeignKey("people.id", ondelete="CASCADE"))
    name = Column(String)
    institution = Column(String)
    level = Column(String)
    address = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    about = Column(String)
    
    person = relationship("people", back_populates="academic_trainings")


class extracurricular_courses(Base):
    __tablename__  = "extracurricular_courses"
    id = Column(Integer, primary_key=True, index=True)
    people_id = Column(Integer, ForeignKey("people.id", ondelete="CASCADE"))
    name = Column(String)
    institution = Column(String)
    level = Column(String)
    address = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    hours = Column(Integer)
    about = Column(String)
    
    person = relationship("people", back_populates="courses")

class experience(Base):
    __tablename__  = "experience"
    id = Column(Integer, primary_key=True, index=True)
    people_id = Column(Integer, ForeignKey("people.id", ondelete="CASCADE"))
    name = Column(String)
    enterprise = Column(String)
    position = Column(String)
    address = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    about = Column(String)
    
    person = relationship("people", back_populates="experiences")

    
class projects(Base):
    __tablename__  = "projects"
    id = Column(Integer, primary_key=True, index=True)
    people_id = Column(Integer, ForeignKey("people.id", ondelete="CASCADE"))
    name = Column(String)
    tags = Column(String)
    resume = Column(String)
    about = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    github = Column(String)
    
    person = relationship("people", back_populates="projects_rel")

    
class technical_skills(Base):
    __tablename__  = "technical_skills"
    id = Column(Integer, primary_key=True, index=True)
    people_id = Column(Integer, ForeignKey("people.id", ondelete="CASCADE"))
    name = Column(String)
    level = Column(String)
    percent_level = Column(Integer)
    
    person = relationship("people", back_populates="skills")


class languages(Base):
    __tablename__  = "languages"
    id = Column(Integer, primary_key=True, index=True)
    people_id = Column(Integer, ForeignKey("people.id", ondelete="CASCADE"))
    name = Column(String)
    level = Column(String)

    person = relationship("people", back_populates="langs")