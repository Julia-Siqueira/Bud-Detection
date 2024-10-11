from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./cana.db' # URL do BD

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}) # conexão com BD

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # permite operações

Base = declarative_base() # import de classes