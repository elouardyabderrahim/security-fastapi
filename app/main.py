from fastapi import FastAPI, Depends
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer
from schemas import UserInDB



#PassLib is a great Python package to handle password hashes.
from passlib.context import CryptContext

SECRET_KEY = "ce041b943239ce78556eafab5766c2d8c107d5b96dd237696cb6cdd0be5671b0"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

# Create a PassLib "context". This is what will be used to hash and verify passwords.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
OAuth2_scheme=OAuth2PasswordBearer(tokenUrl='token')
# Here tokenUrl="token" refers to a relative URL token that we haven't created yet. 
# As it's a relative URL, it's equivalent to ./token.
# Because we are using a relative URL, if your API was located at https://example.com/,
#  then it would refer to https://example.com/token.
app=FastAPI()





def verify_password(plain_password,hashed_password):
    
    return pwd_context.verify(plain_password,hashed_password) 


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db,username:str):
    if username in db:
        user_dict=db[username]
        return UserInDB(**user_dict)

print(OAuth2_scheme.__dict__)







@app.get("/user/me")
async def read_user_me(current_user:Annotated[User,Depends(get_correct_user)]):

    return current_user
    