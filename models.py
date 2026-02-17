from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    tablename = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    language = Column(String, default="kg")

    is_premium = Column(Boolean, default=False)
    premium_type = Column(String, default="free")

    daily_limit = Column(Integer, default=10)
    used_today = Column(Integer, default=0)

    style_counter = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
