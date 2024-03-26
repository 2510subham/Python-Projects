from sqlalchemy import Boolean,Column,Integer,String
from databse import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True)
    hashed_password=Column(String)
    is_active=Column(Boolean,default=True)

class Post(Base):
    __tablename__="Posts"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(50))
    content=Column(String(50))
    