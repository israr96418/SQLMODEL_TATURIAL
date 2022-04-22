# from sqlmodel import SQLModel
# from . import models,database
from models import Book
from database import engine,SQLModel

# def testing():
#     return {"message":"I m used just for testin"}

print("Creating database...")
def create_db_table():
    SQLModel.metadata.create_all(engine)