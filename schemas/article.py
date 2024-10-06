from pydantic import BaseModel

class ArticleBase(BaseModel):
    name: str
    price: int

class ArticleCreate(ArticleBase):
    userId: int

class Article(ArticleBase):
    id: int
    userId: int

    class Config:
        orm_mode = True
        from_attributes = True