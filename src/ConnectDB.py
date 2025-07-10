from sqlalchemy import create_engine, Column, Integer, String, inspect, Date
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def connect_db():
    engine = create_engine(DATABASE_URL)
    insp = inspect(engine)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    base = declarative_base()
    
    return engine, insp, session, base

