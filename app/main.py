from fastapi import FastAPI, Depends
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer


from pydantic import BaseModel

app=FastAPI()



OAuth2_scheme=OAuth2PasswordBearer(tokenUrl='token')
# Here tokenUrl="token" refers to a relative URL token that we haven't created yet. 
# As it's a relative URL, it's equivalent to ./token.
# Because we are using a relative URL, if your API was located at https://example.com/,
#  then it would refer to https://example.com/token.


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return User(
        username=token +"fake_decoded",
        email="john@example.com",
        full_name="John Doe"

    )

print(OAuth2_scheme.__dict__)

async def get_correct_user(token : Annotated [str,Depends(OAuth2_scheme)]):
    
    user=fake_decode_token(token)
    return user


@app.get("/user/me")
async def read_user_me(current_user:Annotated[User,Depends(get_correct_user)]):

    return current_user
    