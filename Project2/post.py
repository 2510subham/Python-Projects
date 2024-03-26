from fastapi import FastAPI,status,HTTPException,APIRouter
from main import db_dependency,modal
from pydantic import BaseModel
post=APIRouter()
class PostBase(BaseModel):
    title:str
    content:str


@post.post("/post/",status_code=status.HTTP_201_CREATED)
async def create_user(post:PostBase,db:db_dependency): # type: ignore
    db_post=modal.Post(**post.dict())
    db.add(db_post)
    db.commit()

@post.get("/post/{post_id}",status_code=status.HTTP_200_OK)
async def get_user(post_id:int,db:db_dependency): # type: ignore
    post=db.query(modal.Post).filter(modal.User.id==post_id).first() # file name and inside that the table name and then we can filter the data
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return post

@post.delete("/post/{post_id}",status_code=status.HTTP_200_OK)
async def get_user(post_id:int,db:db_dependency): # type: ignore
    post=db.query(modal.Post).filter(modal.User.id==post_id).first() # file name and inside that the table name and then we can filter the data
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    db.delete(post)
    return post
