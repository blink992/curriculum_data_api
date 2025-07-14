# API RESTful de Currículos

API desenvolvida em Python com FastAPI e SQLAlchemy para gerenciar informações de pessoas e montar currículos dinamicamente.

## Descrição

Esta API conecta-se a um banco de dados que armazena informações de várias pessoas, permitindo que clientes (como aplicações web em HTML/JS) façam requisições para recuperar dados e montar currículos personalizados. Ideal para integração com sites de portfólio, sistemas de RH e outras aplicações.

---

## Funcionalidades

* CRUD completo de pessoas e seus dados pessoais
* Consulta personalizada para recuperar informações e montar currículos
* Integração simples com frontends via requisições HTTP
* Uso de SQLAlchemy para abstração do banco de dados
* Documentação automática via Swagger UI

---

## Tecnologias

* Python 3.x
* FastAPI
* SQLAlchemy ORM
* Pydantic (schemas de validação)
* Uvicorn (servidor ASGI)

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/blink992/curriculum_data_api.git
cd NomeDoRepositorio
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente (ex: arquivo `.env`) com suas credenciais de banco.

---

## Uso

1. Inicie o servidor:

```bash
uvicorn main:app --reload
```


2. Faça requisições para os endpoints para criar, ler, atualizar e deletar informações de pessoas.

---
