from datetime import date
from pydantic import BaseModel

class InteractionBase(BaseModel):
    doctor_name: str
    hospital: str
    interaction_type: str
    visit_date: date
    discussion: str
    product: str
    summary: str
    followup: date
    notes: str


class InteractionCreate(InteractionBase):
    pass


class InteractionResponse(InteractionBase):
    id: int

    class Config:
        from_attributes = True