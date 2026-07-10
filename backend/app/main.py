from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.database import Base, engine
from app.routers import interactions
from app.graph import graph

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="AI CRM API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(interactions.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "AI CRM Backend Running Successfully"}

# Chat request model
class ChatRequest(BaseModel):
    message: str

# AI Chat endpoint using LangGraph
@app.post("/chat")
def chat(request: ChatRequest):
    result = graph.invoke(
        {
            "message": request.message,
            "response": ""
        }
    )

    return {
        "response": result["response"]
    }