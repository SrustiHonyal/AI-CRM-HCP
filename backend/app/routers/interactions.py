from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/interactions", tags=["Interactions"])


@router.get("/", response_model=list[schemas.InteractionResponse])
def get_all(db: Session = Depends(get_db)):
    return crud.get_interactions(db)


@router.post("/", response_model=schemas.InteractionResponse)
def create(data: schemas.InteractionCreate, db: Session = Depends(get_db)):
    return crud.create_interaction(db, data)