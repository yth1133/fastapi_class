from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, Session

from model import UserTable
import datetime
import uuid

## 처음 데이터베이스에 테이블 만들때 실행하세요

DB_USER = 'yth_api'
DB_PASSWORD = 'yth_pwd'
DB_HOST = '127.0.0.1'  # 예: localhost
DB_PORT = 3306  # 예: 3306
DB_NAME = 'fastapi_db'


# 데이터베이스 url 예시
# DATABASE = "mysql://yth_test:yth_pwd@127.0.0.1/fastapi_db?charset=utf8mb4//"
# DATABASE = f"mysql://{user_name}:{user_pwd}@{db_host}/{db_name}?charset=utf8mb4"


# 연결 문자열 생성
DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# 데이터베이스 연결 생성
engine = create_engine(
    DATABASE_URI,
    echo=True
)

# 데이터베이스 연결 테스트
try:
    conn = engine.connect()
    print("MySQL Database 연결 성공!")
except Exception as e:
    print("MySQL Database 연결 실패!")
    print(e)
finally:
    conn.close()


# 이부분은 데이터베이스에 테이블 생성코드
Base_setting = declarative_base()

# 기본 
class setting_Table(Base_setting):
    __tablename__ = "user"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

class setting_Table2(Base_setting):
    __tablename__ = "mediapipe_data"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = Column(String(50), nullable=False)
    dir = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


Base_setting.metadata.create_all(bind=engine)

# SQLAlchemy ORM으로 데이터베이스에 연결
db_setting_test = Session(bind=engine)

# users 테이블에 있는 모든 레코드 조회 - 제대로 테이블이 만들어졌는지 확인하기 위함.
users = db_setting_test.query(setting_Table2).all()
print("유저 테이블 조회", users)

# 조회된 레코드들 출력
for user in users:
    print('id is :', user.id)
    print('name is :', user.name)
    print(user.age, user.created_at, user.updated_at)
db_setting_test.close()