from sqlalchemy.orm import Session
from repository import articleRepository
from models.article import Article

def create_article(db: Session, article: Article):
    return articleRepository.create_article(db, article)

def get_article(db: Session, article_id: int):
    return articleRepository.get_article(db, article_id)

def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return articleRepository.get_articles(db, skip, limit)

def update_article(db: Session, article_id: int, name: str, price: int):
    return articleRepository.update_article(db, article_id, name, price)

def delete_article(db: Session, article_id: int):
    return articleRepository.delete_article(db, article_id)