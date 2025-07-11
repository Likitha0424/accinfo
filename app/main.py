from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.patch("/v1/player/{player_id}/account", response_model=dict)
def update_my_account(player_id: int, update: schemas.PlayerUpdateRequest, db: Session = Depends(get_db)):
    player = crud.update_player_account(db, player_id, update)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"message": "Account info updated successfully"}
