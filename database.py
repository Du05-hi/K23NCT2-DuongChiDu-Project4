from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Sử dụng %5C thay cho \ để đảm bảo URL không bị lỗi định dạng
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://DESKTOP-ICPA8AC\SQLEXPRESS/LMS_Project?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"



engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()