from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User as UserModel
from schemas.article import Article as ArticleSchema
from schemas.user import User, UserCreate
import service.userService as userService
from typing import List, Dict, Any

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = userService.get_user_by_account(db, account=user.account)
    if db_user:
        raise HTTPException(status_code=400, detail="Account already registered")
    return userService.create_user(db=db, user=UserModel(**user.dict()))

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = userService.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userService.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, name: str, account: str, password: str, db: Session = Depends(get_db)):
    return userService.update_user(db=db, user_id=user_id, name=name, account=account, password=password)

@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return userService.delete_user(db=db, user_id=user_id)

@router.get("/{user_id}/articles", response_model=Dict[str, Any])
def read_user_articles(user_id: int, db: Session = Depends(get_db)):
    db_user = userService.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    articles = [ArticleSchema.from_orm(article) for article in db_user.articles]
    return {"user_name": db_user.name, "articles": articles}