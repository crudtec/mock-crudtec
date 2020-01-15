from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI()

@app.get("/")
def read_root():
    response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/root.json")
    return json.loads(response.content)

#AUTH
class auth(BaseModel):
    user: str
    password: str

@app.post("/auth", status_code=200)
async def create_item(item: auth):
    if item.user == "admin@crudtec.com.br":
        response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/auth-admin.json")
        return json.loads(response.content)
    elif item.user == "staff@crudtec.com.br":
        response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/auth-staff.json")
        return json.loads(response.content)
    else:  
        #Montar json do operador... (usuario penas com o chat)
        response = requests.get("https://s3.amazonaws.com/crudtec.com.br/mock-mflow/auth-staff.json")
        return json.loads(response.content)

    

#DASHBOARD



