from sqlalchemy.orm import Session
from models.article import Article

def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Article).offset(skip).limit(limit).all()

def create_article(db: Session, article: Article):
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def update_article(db: Session, article_id: int, name: str, price: int):
    article = db.query(Article).filter(Article.id == article_id).first()
    if article:
        article.name = name
        article.price = price
        db.commit()
        db.refresh(article)
    return article

def delete_article(db: Session, article_id: int):
    article = db.query(Article).filter(Article.id == article_id).first()
    if article:
        db.delete(article)
        db.commit()
    return article