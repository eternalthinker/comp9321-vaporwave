from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app import app

Base = declarative_base()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = db_session.query_property()

def init_db():
   # create tables
   Base.metadata.create_all(bind=engine)
