from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# 從 .env 文件中加載環境變量
load_dotenv()

# 從環境變量中獲取資料庫連接詳細信息
db_url = os.getenv("DATABASE_URL")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

# 構建完整的資料庫 URL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_username}:{db_password}@{db_url}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()