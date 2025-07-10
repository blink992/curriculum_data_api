from typing import List
from api import *
from database import *
from models.models import *
from schemas.models import *

@app.get("/pt/aboutMe", response_model=List[peopleOut])
def get_aboutMe_pt(db: Session = Depends(get_db)):
    return db.query(people).all()

    
# @app.get("pt/aboutMe")
# def get_aboutMe_en():
#     return {"aboutMe": """Apaixonado por jogos e tecnologia desde a infância, iniciei meus estudos em programação por conta própria aos 12 anos.
#             Participei de projetos de robótica com Arduino nas eletivas do Ensino Médio e desenvolvi jogos em Python e aplicações web como 
#             projetos pessoais. Atualmente curso Sistemas de Informação e atuo como estagiário na Prefeitura de Vitória, com foco em manutenção 
#             de sistemas web e desenvolvimento Full Stack. Tenho interesse em desenvolvimento full stack e criação de jogos com C++ e Unreal Engine."""}

# @app.get("en/academicBackground")
# def get_academicBackground_en():
#     return {"academicBackground": []}

# @app.get("pt/academicBackground")

