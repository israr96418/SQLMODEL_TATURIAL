# SQLMODEL_TATURIAL

Difference b/w one first and one_none:
first(): we create a table of student and insert data, after that we 
read from table with the query (# result = session.exec(select(Book).where(Book.name==book_name)).first())
for example different student have sama name so this query will be
select the name which come in first:if there is no matching then it will be return
none:

one():
result = session.exec(select(Book).where(Book.name==book_name)).one()
this query will be match only with one row over all the table if they find out 
multiple row with the same name it will be return error:
and if the not found any row they also return error:

one_none():
result = session.exec(select(Book).where(Book.id==book_id)).one_or_none()
this will be perfect one b/z this query will be match with one row in over all the table
if the find out it will be return the result otherwise it will be go the else: part
