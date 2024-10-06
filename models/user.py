from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    account = Column(String(50), unique=True, index=True)
    password = Column(String(50))

    articles = relationship("Article", back_populates="user")