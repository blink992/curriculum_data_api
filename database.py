from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from dotenv import load_dotenv
import os
from models.models import Base

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Database URL: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)    
Base.metadata.create_all(bind=engine)


# Aqui criamos uma função que será chamada por FastAPI
def get_db():
    db = session()
    try:
        yield db  # entrega o objeto para uso no endpoint
    finally:
        db.close()  # garante o fechamento da conexão após a resposta