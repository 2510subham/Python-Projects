from fastapi import FastAPI,HTTPException,Depends,status
from Pydantic import BaseModel
import models
from typing import Annotated
from databse import sessionLocal,engine
from sqlalchemy.orm import Session

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

#app.include_router(router, prefix="/items")   for app routing

class PostBase(BaseModel):
    title:str
    content:str

class UserBase(BaseModel):
    name:str

def getDb():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
    
db_dependency=Annotated(Session,Depends(getDb))

@app.post("/post/",status_code=status.HTTP_201_CREATED)
async def create_user(post:PostBase,db:db_dependency): # type: ignore
    db_post=models.Post(**post.dict())
    db.add(db_post)
    db.commit()

@app.get("/posts/{post_id}",status_code=status.HTTP_200_OK)
async def get_user(post_id:int,db:db_dependency): # type: ignore
    post=db.query(models.Post).filter(models.User.id==post_id).first() # file name and inside that the table name and then we can filter the data
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return post

@app.delete("/posts/{post_id}",status_code=status.HTTP_200_OK)
async def get_user(post_id:int,db:db_dependency): # type: ignore
    post=db.query(models.Post).filter(models.User.id==post_id).first() # file name and inside that the table name and then we can filter the data
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    db.delete(post)
    return post

@app.post("/post/",status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase,db:db_dependency): # type: ignore
    db_user=models.User(**user.dict())
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id}",status_code=status.HTTP_200_OK)
async def get_user(user_id:int,db:db_dependency): # type: ignore
    user=db.query(models.User).filter(models.User.id==user_id).first() # file name and inside that the table name and then we can filter the data
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user
    
    

