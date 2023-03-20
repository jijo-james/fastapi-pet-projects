from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]


    class config:
        orm_mode = True
        schema_extra = {
            'example':{
                'username':'jijo',
                'email':'me@jijo.dev',
                'password':'password',
                'is_staff':False,
                'is_active':True
            }
        }


class Settings(BaseModel):
    authjwt_secret_key:str = '8291c8ae75f9b8bca9584b786c0b8bbdcc28b619868b609187d6547bbc0496d7'


class LoginModel(BaseModel):
    username:str
    password:str

    