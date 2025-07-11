from sqlalchemy import Column, Integer, String
from .database import Base

class Player(Base):
    __tablename__ = "player"

    player_id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=True)
    favourite_club = Column(String, nullable=True)
    favourite_player = Column(String, nullable=True)
    position = Column(String, nullable=True)
    preferred_foot = Column(String, nullable=True)
    favourite_country = Column(String, nullable=True)
    location = Column(String, nullable=True)
