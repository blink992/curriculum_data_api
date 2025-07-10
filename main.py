from src.ConnectAPI import connect_API
from src.ConnectDB import connect_db
from src.models import *
app = connect_API()
engine, session, base = connect_db()



@app.get("/pt/aboutMe/")
def get_aboutMe_pt():
    db = session()
    pessoas = db.query(people).all()
    db.close()
    return [
            {
            "name": p.name,
            "positions": p.positions,
            "about": p.about,
            "address": p.address,
            "phone_01": p.phone_01,
            "phone_02": p.phone_02,
            "mail": p.mail,
            "linkedin": p.linkedin
            } for p in pessoas
            ]
    
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

