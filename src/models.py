import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(Integer, nullable=False, unique=False)
    email = Column(String(250), nullable=False, unique=True)
    rel = relationship("posts")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))


class SavedPost(Base):
    __tablename__ = "savedposts"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

class Comment(Base):
    __tablename__ = "comments" 
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    bodytext = Column(String(500))

 
class Follower(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("users.id"))
    user_to_id = Column(Integer, ForeignKey("users.id"))   

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
