from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir qualquer origem (cuidado em produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique ex: ["https://meusite.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"mensagem": "atualizou"}
