from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the State class
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    # Create an instance of declarative_base
    Base = declarative_base()

if __name__ == "__main__":
    # Replace these with your MySQL credentials and database name
    mysql_username = "your_username"
    mysql_password = "your_password"
    database_name = "your_database"

    # Create a MySQL connection
    engine = create_engine(f"mysql://{mysql_username}:{mysql_password}@localhost:3306/{database_name}")
    
    # Create all tables defined by the classes that inherit from Base
    Base.metadata.create_all(engine)
