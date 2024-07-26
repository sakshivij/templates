from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..config import EnvironmentVariables
from ..model.base import Base

env = EnvironmentVariables()
DATABASE_URL = env.database_url

class Database:
    def __init__(self, database_url=DATABASE_URL):
        self.database_url = database_url
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.init_db()

    def init_db(self):
        Base.metadata.create_all(bind=self.engine)

# Create a database instance
database = Database()

# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
