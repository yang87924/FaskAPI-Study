from sqlalchemy.orm import Session
from models.user import User

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_account(db: Session, account: str):
    return db.query(User).filter(User.account == account).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user_id: int, name: str, account: str, password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.account = account
        user.password = password
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user