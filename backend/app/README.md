# AI-First CRM - HCP Interaction Module

## Overview

AI-First CRM is a Healthcare Professional (HCP) interaction management system.
It allows field representatives to log, search, summarize and manage doctor interactions using an AI assistant.

## Features

- HCP interaction dashboard
- Log doctor visits
- AI Chat interface
- LangGraph AI Agent
- Groq LLM integration (gemma2-9b-it)
- MySQL database integration

## AI Agent Tools

1. Log Interaction
2. Edit Interaction
3. Search Interaction
4. Sales Summary
5. Follow-up Reminder

## Tech Stack

### Frontend
- React
- Redux
- Google Inter Font

### Backend
- FastAPI
- Python
- LangGraph

### AI
- Groq LLM
- gemma2-9b-it

### Database
- MySQL

## Run Backend

```bash
cd backend

python -m venv .venv

pip install -r requirements.txt

uvicorn app.main:app --reload