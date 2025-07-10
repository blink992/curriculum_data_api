from src.ConnectAPI import connect_API
from src.ConnectDB import connect_db

app = connect_API()
engine, insp, session, base = connect_db()



@app.get("/pt/aboutMe/")
def get_aboutMe_pt():
    
    return {"aboutMe": """Passionate about games and technology since childhood, I began studying programming on my own at the age of 12. 
            I participated in robotics projects using Arduino during technical school and developed games in Python and web applications 
            as personal projects. I am currently pursuing a degree in Information Systems and working as an intern at the Municipality of Vitória,
            focusing on maintaining web systems. I have a strong interest in full stack development and game creation using C++ and Unreal Engine."""}
    
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

