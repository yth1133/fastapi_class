from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DB_USER = 'yth_api'
DB_PASSWORD = 'yth_pwd'
DB_HOST = '127.0.0.1'  # 예: localhost
DB_PORT = 3306  # 예: 3306
DB_NAME = 'fastapi_db'


# 데이터베이스 url 예시
# DATABASE = "mysql://yth_test:yth_pwd@127.0.0.1/fastapi_db?charset=utf8mb4//"

# DATABASE = f"mysql://{user_name}:{user_pwd}@{db_host}/{db_name}?charset=utf8mb4"


# 연결 문자열 생성
DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4'

ENGINE = create_engine(
    DATABASE_URI,
    echo=True
)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()

