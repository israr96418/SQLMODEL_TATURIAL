from sqlmodel import SQLModel,create_engine
import os


BASE_DIR=os.path.dirname(os.path.realpath(__file__))
print("base_dir: ",BASE_DIR)

# connection string to database
connt_str = "sqlite:///"+os.path.join(BASE_DIR,'books.db')
print("connection string: ",connt_str)

# echo=True
# It will make the engine print all the SQL statements
# it executes, which can help you understand what's happening.
# it is particulary useful for learing and debugging

# It is an object that handles the communication with the database.
# You should normally have a single engine object for your whole application and re-use it everywhere.
# echo=True
# It will make the engine print all the SQL statements
# it executes, which can help you understand what's happening.
# it is particulary useful for learing and debugg


engine = create_engine(connt_str,echo=True)
print("Engine",engine)