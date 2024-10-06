from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    price = Column(Integer)
    userId = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="articles")