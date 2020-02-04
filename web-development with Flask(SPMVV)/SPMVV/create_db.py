from sqlalchemy import Column,String,Integer

# create_engine --> create database file with database language
from sqlalchemy import create_engine

# maping classes(tables)
from sqlalchemy.ext.declarative import declarative_base

# create declarative_base object
Base = declarative_base()

class User(Base):
	__tablename__ ='users'
	id =Column(Integer,primary_key= True)
	name =Column(String(35),nullable =False)
	email =Column(String(30),nullable=False,unique=True)
	mobile =Column(Integer,nullable=False)
	password=Column(String(30),nullable=False)

# assign the name to database with type of database language
engine = create_engine('sqlite:///mydb.db')

Base.metadata.create_all(engine)

print('database Created Successfully.')

