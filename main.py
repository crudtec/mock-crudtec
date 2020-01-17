from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import requests
import json


app = FastAPI(
    title="M-Flow - Mock",
    description="Este e o mock para desenvolvermos o M-Flow",
    version="0.0.1",
)
origins = [
    "http://localhost:3000",
    "https://mflow-crudtec.herokuapp.com/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#AUTH
class auth(BaseModel):
    user: str
    password: str

@app.post("/auth", status_code=200, tags=["Autenticate"],
summary="Realiza a autenticacao",
description="Autentica, responde com token JWT e caracteristicas do usuario (perfil e tema)")
async def post_auth(auth: auth):
    if auth.user == "admin@crudtec.com.br":
        response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/auth-admin.json")
        return json.loads(response.content)
    if auth.user == "staff@crudtec.com.br":
        response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/auth-staff.json")
        return json.loads(response.content)
    if auth.user == "agent@crudtec.com.br":
        response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/auth-agent.json")
        return json.loads(response.content)
    if auth.user == "superadmin@crudtec.com.br":
        response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/auth-superadmin.json")
        return json.loads(response.content)

#TICKETS
class session(BaseModel):
    toId:str
    toName:str
    fromId:str
    fromName:str
    serviceUrl:str
    channelId:str
    conversationId:str

class ticket(BaseModel):
    ticketNumber: int
    userName: str
    channel:str
    sessionInformation:session
    created:str
    finished:str

@app.post("/tickets", status_code=201, tags=["Tickets"],
summary="Insere um novo ticket",
description="Responsavel por criar novos tickets.")
async def post_ticket(ticket: ticket):
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/ticket-post.json")
    return json.loads(response.content)

@app.put("/tickets/{ticketNumber}", status_code=204, tags=["Tickets"],
summary="Atualiza um ticket",
description="Responsavel por atuliazr os tickets.")
async def put_ticket(ticket: ticket):
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/ticket-put.json")
    return json.loads(response.content)

class conversation(BaseModel):
    text:str
    intent:str
    who:str
    ticketNumber:str
    dateTime:str

@app.post("/conversations", status_code=201,  tags=["Conversations"],
summary="Insere uma nova frase da conversa em um ticket",
description="Responsavel por criar nova conversa relacionada a um ticket aberto.")
async def post_conversation(conversation: conversation):
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/conversation.json")
    return json.loads(response.content)

@app.get("/conversations/{ticketNumber}", status_code=200, tags=["Conversations"],
summary="Resgata um vetor de toda conversa",
description="Responsavel por resgatar a lista de uma conversa ate o momento.")
async def get_conversation(conversation: conversation):
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#GET PARAMETERS
@app.get("/parameters", status_code=200, tags=["Parameters"],
summary="Resgata parametros",
description="Responsavel por resgatar os parametros da aplicacao")
def get_par():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#POST PARAMETER
@app.post("/parameters", status_code=200, tags=["Parameters"],
summary="Insere parametros",
description="Responsavel por criar parametros da aplicacao")
def post_par():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#PUT PARAMETER
@app.put("/parameters/{parameterId}", status_code=204, tags=["Parameters"],
summary="Atualiza parametros",
description="Responsavel por atualizar o parametro da aplicacao")
def put_par():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#DELETE PARAMETER
@app.delete("/parameters/{parameterId}", status_code=200, tags=["Parameters"],
summary="Exclui parametros",
description="Responsavel por excluir o parametro da aplicacao. **Devera apenas desativar o registro**")
def del_par():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#GET USERS
@app.get("/users", status_code=200, tags=["Users"],
summary="Resgata usuarios",
description="Responsavel por resgatar os usuarios da aplicacao")
def get_usr():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#POST USER
@app.post("/users", status_code=200, tags=["Users"],
summary="Insere usuario",
description="Responsavel por criar usuario da aplicacao")
def post_usr():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#PUT USER
@app.put("/users/{userId}", status_code=204, tags=["Users"],
summary="Atualiza usuario",
description="Responsavel por atualizar o usuario da aplicacao")
def put_usr():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#DELETE USER
@app.delete("/parameters/{userId}", status_code=200, tags=["Users"],
summary="Exclui usuario",
description="Responsavel por excluir o usuario da aplicacao. **Devera apenas desativar o registro**")
def del_usr():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)


#GET CLIENTS
@app.get("/clients", status_code=200, tags=["Clients"],
summary="Resgata clientes",
description="Responsavel por resgatar os clientes da aplicacao")
def get_clt():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#POST CLIENT
@app.post("/clients", status_code=200, tags=["Clients"],
summary="Insere cliente",
description="Responsavel por criar usuario da aplicacao")
def post_clt():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#PUT CLIENT
@app.put("/clients/{clientId}", status_code=204, tags=["Clients"],
summary="Atualiza cliente",
description="Responsavel por atualizar o cliente da aplicacao")
def put_clt():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#DELETE CLIENT
@app.delete("/clients/{clientId}", status_code=200, tags=["Clients"],
summary="Exclui cliente",
description="Responsavel por excluir o cliente da aplicacao. **Devera apenas desativar o registro**")
def del_clt():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)


#GET PROJECTS
@app.get("/projects", status_code=200, tags=["Projects"],
summary="Resgata projetos",
description="Responsavel por resgatar os projetos de um cliente da aplicacao")
def get_prj():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#POST PROJECT
@app.post("/projects", status_code=200, tags=["Projects"],
summary="Insere projeto",
description="Responsavel por criar projeto da aplicacao")
def post_prj():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#PUT PROJECT
@app.put("/projects/{projectId}", status_code=204, tags=["Projects"],
summary="Atualiza projeto",
description="Responsavel por atualizar o projeto da aplicacao")
def put_prj():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)

#DELETE PROJECT
@app.delete("/projects/{projectId}", status_code=200, tags=["Projects"],
summary="Exclui projeto",
description="Responsavel por excluir o projetoda aplicacao. **Devera apenas desativar o registro**")
def del_prj():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/construction.json")
    return json.loads(response.content)


#GET DASH
@app.get("/dashboard", status_code=200, tags=["Dasboards"],
summary="Resgata dashboard",
description="Responsavel por resgatar as informacoes do dashboard")
def get_dash():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/root.json")
    return json.loads(response.content)


#GET DEFAULT
@app.get("/", tags=["Root"]) 
def read_root():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/root.json")
    return json.loads(response.content)


