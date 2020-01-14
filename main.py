from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Mock CrudTec"}

#AUTH
class auth(BaseModel):
    user: str
    password: str

@app.post("/auth", status_code=200)
async def create_item(item: auth):
    if item.user == "admin@crudtec.com.br":
        return {
            "access_token": "exemplo-yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1Njk0NjM5NDUsImlzcyI6IkNydWRUZWMiLCJhdWQiOiJDbGllbnRzIn0.wzjfA8OAk06SGAEUyiDiRokyu54BrJqFsg-XzSI-8GU",
            "user": {
                "uuid"    : 'XgbuVEXBU5gtSKdbQRP1Zbbby1i1',
                "from"    : 'db-users',
                "password": "admin",
                "role"    : "admin",
                "data"    : {
                    'displayName': 'Wlad Adm',
                    'photoURL'   : 'https://i.pinimg.com/originals/d1/1a/45/d11a452f5ce6ab534e083cdc11e8035e.png',
                    'email'      : 'admin',
                    "settings"     : {
                        "layout"          : {
                            "style" : 'layout1',
                            "config": {
                                "scroll" : 'content',
                                "navbar" : {
                                    "display" : True,
                                    "folded"  : True,
                                    "position": 'left'
                                },
                                "toolbar": {
                                    "display" : True,
                                    "style"   : 'fixed',
                                    "position": 'below'
                                },
                                "footer" : {
                                    "display" : True,
                                    "style"   : 'fixed',
                                    "position": 'below'
                                },
                                "mode"   : 'fullwidth'
                            }
                        },
                        "customScrollbars": True,
                        "theme"           : {
                            "main"   : 'defaultDark',
                            "navbar" : 'defaultDark',
                            "toolbar": 'defaultDark',
                            "footer" : 'defaultDark'
                        }
                    },
                    "shortcuts"    : [
                        'calendar',
                        'mail',
                        'contacts'
                    ]
                }
            }
        }
    elif item.user == "staff@crudtec.com.br":
         return {
            "access_token": "exemplo-yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1Njk0NjM5NDUsImlzcyI6IkNydWRUZWMiLCJhdWQiOiJDbGllbnRzIn0.wzjfA8OAk06SGAEUyiDiRokyu54BrJqFsg-XzSI-8GU",
            
            
            "user": {
                "uuid"    : 'XgbuVEXBU6gtSKdbTYR1Zbbby1i3',
                "from"    : 'custom-db',
                "password": "staff",
                "role"    : "staff",
                "data"    : {
                    'displayName': 'Wlad Staff',
                    'photoURL'   : 'https://img.icons8.com/plasticine/2x/user.png',
                    'email'      : 'staff',
                    "settings"     : {
                        "layout"          : {
                            "style" : 'layout2',
                            "config": {
                                "mode"   : 'boxed',
                                "scroll" : 'content',
                                "navbar" : {
                                    "display": True
                                },
                                "toolbar": {
                                    "display" : True,
                                    "position": 'below'
                                },
                                "footer" : {
                                    "display": True,
                                    "style"  : 'fixed'
                                }
                            }
                        },
                        "customScrollbars": True,
                        "theme"          : {
                            "main"   : 'greeny',
                            "navbar" : 'mainThemeDark',
                            "toolbar": 'mainThemeDark',
                            "footer" : 'mainThemeDark'
                        }
                    },
                    shortcuts    : [
                        'calendar',
                        'mail',
                        'contacts',
                        'todo'
                    ]
                }
            }
        }
    else:  
        response = requests.get("https://viacep.com.br/ws/01001000/json/")
        return json.loads(response.content)

    

#DASHBOARD



