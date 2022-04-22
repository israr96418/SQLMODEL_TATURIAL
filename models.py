from typing import Optional

from sqlmodel import SQLModel,Field


# these are the sqlmodel
# sqlmodel are design just like pydantic
# means this model are as pydantic model as well as sqlalchemy model
class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str

class Books(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str

