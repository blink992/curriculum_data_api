from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from src.models import Base

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def connect_db():
    engine = create_engine(DATABASE_URL)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base.metadata.create_all(bind=engine)

    return engine, session, Base

