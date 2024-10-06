from sqlalchemy.orm import Session
from repository import userRepository
from models.user import User

def create_user(db: Session, user: User):
    return userRepository.create_user(db, user)

def get_user(db: Session, user_id: int):
    return userRepository.get_user(db, user_id)

def get_user_by_account(db: Session, account: str):
    return userRepository.get_user_by_account(db, account)

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return userRepository.get_users(db, skip, limit)

def update_user(db: Session, user_id: int, name: str, account: str, password: str):
    return userRepository.update_user(db, user_id, name, account, password)

def delete_user(db: Session, user_id: int):
    return userRepository.delete_user(db, user_id)