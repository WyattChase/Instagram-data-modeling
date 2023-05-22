import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    nickname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, primary_key=True)
    password = Column(String(250), nullable=False, primary_key=True)
    following = Column(Integer, nullable=True)
    followers = Column(Integer, nullable=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    profile_name = Column(String(250), ForeignKey('user.id'))
    title = Column(String(250), nullable=False)
    content = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=True)
    comments = Column(Integer, nullable=True)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Like(Base):
    __tablename__ = 'likes'
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.nickname'))
    user = relationship('User')
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')
    comments_id = Column(Integer, ForeignKey('comments.id'))
    comments = relationship('Comments')

class Follow(Base):
    __tablename__ = 'followers'
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.nickname'))
    user_to_id = Column(Integer, ForeignKey('user.nickname'))
    user = relationship('User')

class Following(Base):
    __tablename__ = 'following'
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.nickname'))
    user_to_id = Column(Integer, ForeignKey('user.nickname'))
    user = relationship('User')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
