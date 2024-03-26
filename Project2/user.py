from fastapi import FastAPI,status,HTTPException,APIRouter
from main import db_dependency,modal
from pydantic import BaseModel

user=APIRouter()


class UserBase(BaseModel):
    name:str


@user.post("/user/",status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase,db:db_dependency): # type: ignore
    db_user=modal.User(**user.dict())
    db.add(db_user)
    db.commit()

@user.get("/user/{user_id}",status_code=status.HTTP_200_OK)
async def get_user(user_id:int,db:db_dependency): # type: ignore
    user=db.query(modal.User).filter(modal.User.id==user_id).first() # file name and inside that the table name and then we can filter the data
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user
    
    
