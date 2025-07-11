from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def update_player_account(db: Session, player_id: int, update: schemas.PlayerUpdateRequest):
    player = db.query(models.Player).filter(models.Player.player_id == player_id).first()
    if not player:
        return None

    if update.password:
        player.password = pwd_context.hash(update.password)
    if update.favourite_club:
        player.favourite_club = update.favourite_club
    if update.favourite_player:
        player.favourite_player = update.favourite_player
    if update.position:
        player.position = update.position
    if update.preferred_foot:
        player.preferred_foot = update.preferred_foot
    if update.favourite_country:
        player.favourite_country = update.favourite_country
    if update.location:
        player.location = update.location

    db.commit()
    db.refresh(player)
    return player
