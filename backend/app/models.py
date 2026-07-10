from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    doctor_name = Column(String(200))
    hospital = Column(String(200))
    interaction_type = Column(String(100))

    visit_date = Column(Date)

    discussion = Column(Text)

    product = Column(String(200))

    summary = Column(Text)

    followup = Column(Date)

    notes = Column(Text)