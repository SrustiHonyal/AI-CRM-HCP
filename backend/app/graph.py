from langgraph.graph import StateGraph, END

from app.state import CRMState
from app.tools import (
    log_interaction,
    edit_interaction,
    search_interaction,
    followup_reminder,
    sales_summary,
)
from app.agent import ask_ai


def router(state: CRMState):

    msg = state["message"].lower()

    if "log" in msg:
        return {
            "message": state["message"],
            "response": log_interaction.invoke(state["message"])
        }

    elif "edit" in msg:
        return {
            "message": state["message"],
            "response": edit_interaction.invoke(state["message"])
        }

    elif "search" in msg or "show" in msg:
        return {
            "message": state["message"],
            "response": search_interaction.invoke(state["message"])
        }

    elif "follow" in msg:
        return {
            "message": state["message"],
            "response": followup_reminder.invoke("")
        }

    elif (
        "summary" in msg
        or "summarize" in msg
        or "previous visit" in msg
        or "previous visits" in msg
        or "history" in msg
    ):
        return {
            "message": state["message"],
            "response": sales_summary.invoke("")
        }

    else:
        reply = ask_ai(state["message"])

        return {
            "message": state["message"],
            "response": reply
        }


workflow = StateGraph(CRMState)

workflow.add_node("router", router)

workflow.set_entry_point("router")

workflow.add_edge("router", END)

graph = workflow.compile()