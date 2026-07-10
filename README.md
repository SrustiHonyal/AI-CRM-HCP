# AI CRM HCP Module

## Project Overview

The AI CRM HCP Module is an AI-first Customer Relationship Management (CRM) application designed for Healthcare Professionals (HCPs). It helps medical sales representatives manage doctor interactions using both a structured interaction form and an AI-powered conversational chat interface.

The application uses LangGraph as the AI agent framework and Groq's Gemma2-9B-IT large language model to understand user requests and perform CRM operations.

---

## Tech Stack

### Frontend
- React
- Redux
- Vite
- Google Inter Font

### Backend
- Python
- FastAPI

### AI
- LangGraph
- Groq API
- Gemma2-9B-IT LLM

### Database
- MySQL

---

## Features

- Dashboard
- HCP Interaction Management
- AI Chat Interface
- Log Interaction Tool
- Edit Interaction Tool
- Search Interaction Tool
- Follow-up Reminder Tool
- Sales Summary Tool
- MySQL Database Integration

---

## LangGraph Agent

The LangGraph agent acts as the intelligent decision-making layer of the application.

Based on the user's message, it automatically routes the request to the appropriate CRM tool.

Supported tools include:

1. Log Interaction
2. Edit Interaction
3. Search Interaction
4. Follow-up Reminder
5. Sales Summary

---

## Project Structure

```
AI-CRM-HCP/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── graph.py
│   │   ├── tools.py
│   │   ├── agent.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── routers/
│   │   └── ...
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── redux/
│   │   ├── services/
│   │   └── ...
│   └── package.json
│
├── sqldb.sql
└── README.md
```

---

## Database Setup

Create the database:

```sql
CREATE DATABASE ai_crm;
```

Select database:

```sql
USE ai_crm;
```

Import the provided SQL file:

```
sqldb.sql
```

---

## Backend Setup

Navigate to the backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger API:

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the React application:

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## AI Chat Examples

### Log Interaction

```
Log interaction with Dr. Rajesh Kumar at Apollo Hospital. Discussed Medicine A.
```

### Edit Interaction

```
Edit latest interaction notes: Share clinical trial data.
```

### Search Interaction

```
Search Dr. Rajesh Kumar
```

### Follow-up Reminder

```
Show follow up reminders
```

### Sales Summary

```
Summarize previous visits
```

---

## API Endpoints

### GET

```
/
```

Returns backend status.

### GET

```
/interactions
```

Returns all HCP interactions.

### POST

```
/interactions
```

Creates a new interaction.

### POST

```
/chat
```

Processes AI chat requests through LangGraph.

---

## Assignment Requirements Covered

- React Frontend
- Redux State Management
- FastAPI Backend
- LangGraph AI Agent
- Groq Gemma2-9B-IT Integration
- MySQL Database
- AI Chat Screen
- Log Interaction
- Edit Interaction
- Search Interaction
- Follow-up Reminder
- Sales Summary

---

## Author

**Srusti Honyal**

MCA Final Year Student

AI CRM HCP Module Assignment
