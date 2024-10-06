from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.article import Article as ArticleModel
from schemas.article import Article, ArticleCreate
import service.articleService as articleService
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Article)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    return articleService.create_article(db=db, article=ArticleModel(**article.dict()))

@router.get("/", response_model=List[Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    articles = articleService.get_articles(db, skip=skip, limit=limit)
    return articles

@router.get("/{article_id}", response_model=Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = articleService.get_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@router.put("/{article_id}", response_model=Article)
def update_article(article_id: int, name: str, price: int, db: Session = Depends(get_db)):
    return articleService.update_article(db=db, article_id=article_id, name=name, price=price)

@router.delete("/{article_id}", response_model=Article)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    return articleService.delete_article(db=db, article_id=article_id)