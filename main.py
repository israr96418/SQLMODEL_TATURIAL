from typing import List

from fastapi import FastAPI, status, HTTPException
from sqlmodel import Session, select

# from create_db import testing
from database import engine
from models import Book

app = FastAPI()
# data=testing()
# print("data from create_db:",data)

session = Session(bind=engine)


@app.get("/books", response_model=List[Book], status_code=status.HTTP_200_OK)
def get_all_book():
    # statement = select(Book)
    # print("statment", statement)

    # compact version
    result = session.exec(select(Book)).all()
    return result


@app.get("/book/{book_id}")
def get_all_book(book_id: int):
    # two way to get data from database:
    # first one
    # statment = select(Book).where(Book.id == book_id)
    # result = session.exec(statment).first()

    # second one
    result = session.get(Book, book_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Your Book with Id '{book_id}' is not found")


@app.post("/book", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    new_entry = Book(title=book.title, description=book.description)
    session.add(new_entry)
    session.commit()

    return new_entry


@app.put("/book/{book_id}", response_model=Book)
def update(book_id: int, book: Book):
    # statment = select(Book).where(Book.id == book_id)
    # result = session.exec(statment).first()

    # compact version of the above queries:
    result = session.exec(select(Book).where(Book.id == book_id)).first()

    if result:
        result.title = book.title
        result.description = book.description
        session.commit()
        session.refresh(result)
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{book_id} is not found")


@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    # statement = select(Book).where(Book.id == book_id)
    # result = session.exec(statement).one_or_none()

    # result = session.exec(select(Book).where(Book.id==book_id)).one()
    # result = session.exec(select(Book).where(Book.id==book_id)).first()
    result = session.exec(select(Book).where(Book.id == book_id)).one_or_none()
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{book_id} is not found")
    # session.refresh(result)
    session.delete(result)
    session.commit()

    return {"message": "your post has been successfully deleted"}

# read data with query selector:
# means that put limition on the read of data from table:
@app.get("/books", response_model=List[Book], status_code=status.HTTP_200_OK)
def get_all_book(Limit:int=10,Offset:int=10):
    # statement = select(Book)
    # print("statment", statement)

    # compact version
    result = session.exec(select(Book).limit(Limit).offset(Offset)).all()
    return result
