import sys
#for creating the mapper code
from sqlalchemy import Column, Integer, String, DateTime

#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

#for configuration
from sqlalchemy import create_engine
from datetime import datetime

#create declarative_base instance
Base = declarative_base()

#we'll add classes here
class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, unique=True, nullable=False)
    username = Column(String(80), primary_key=True, unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    date = Column(DateTime, nullable=False, default= datetime.now)

class Upload(Base):
    __tablename__ = 'Uploads'
    id = Column(Integer, unique=True, nullable=False)
    username = Column(String(80), primary_key=True, unique=True, nullable=False)
    filename = Column(String(100), nullable=False)
    filetype = Column(String(20), nullable=False) 
    date = Column(DateTime, nullable=False, default= datetime.now)



class Search(Base):
    __tablename__ = 'Search'
    id = Column(Integer, unique=True, nullable=False)
    username = Column(String(80), primary_key=True, unique=True, nullable=False)
    songname = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False, default= datetime.now)




class SongInfo(Base):
    __tablename__ = 'Songs'
    id = Column(Integer, primary_key=True)
    songname = Column(String(100), nullable=False)
    album = Column(String(100), nullable=False)
    singer = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    lyricist = Column(String(100), nullable=False)
    music_director = Column(String(100), nullable=False)
    
    

    

#creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)

