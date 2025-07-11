from pydantic import BaseModel
from typing import Optional

class PlayerUpdateRequest(BaseModel):
    password: Optional[str]
    favourite_club: Optional[str]
    favourite_player: Optional[str]
    position: Optional[str]
    preferred_foot: Optional[str]
    favourite_country: Optional[str]
    location: Optional[str]
