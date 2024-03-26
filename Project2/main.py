from fastapi import FastAPI,HTTPException,Depends,status
import models
from typing import Annotated
from databse import sessionLocal,engine
from sqlalchemy.orm import Session
from user import user
from post import post
app=FastAPI()
modal=models.Base.metadata.create_all(bind=engine)

def getDb():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
    
db_dependency=Annotated(Session,Depends(getDb))

app.include_router(post, prefix="/post")
app.include_router(user, prefix="/user")

@app.get("/")
async def read_root():
    return {"Hello": "World"}