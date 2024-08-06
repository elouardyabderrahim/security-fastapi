from fastapi import FastAPI, Depends
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer


app=FastAPI()


OAuth2_scheme=OAuth2PasswordBearer(tokenUrl='token')
# Here tokenUrl="token" refers to a relative URL token that we haven't created yet. 
# As it's a relative URL, it's equivalent to ./token.
# Because we are using a relative URL, if your API was located at https://example.com/,
#  then it would refer to https://example.com/token.





@app.get("/user/me")
async def read_utems(token:Annotated[str,Depends(OAuth2_scheme)]):
    return {"token":token}
    