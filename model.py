from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from database import Base
from database import ENGINE
import datetime
import uuid


class UserTable(Base):
    __tablename__ = "user"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    
class User(BaseModel):
    id   : str
    name : str
    age  : int