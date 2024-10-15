from sqlalchemy import Column, Integer, String
from app.database import Base

class Imagem(Base):
    __tablename__ = "imagens"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    caminho = Column(String)
