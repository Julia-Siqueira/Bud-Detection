from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Img_cana(Base):
    __tablename__ = "imagens"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label = Column(String)
    local_imagem = Column(String)
    