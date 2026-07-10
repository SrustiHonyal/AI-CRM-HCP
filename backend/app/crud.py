from sqlalchemy.orm import Session
from app import models, schemas


def get_interactions(db: Session):
    return db.query(models.Interaction).all()


def create_interaction(db: Session, interaction: schemas.InteractionCreate):
    db_interaction = models.Interaction(**interaction.model_dump())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction