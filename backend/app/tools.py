from langchain_core.tools import tool
from app.database import get_connection


@tool
def log_interaction(details: str) -> str:
    """
    Log a new HCP interaction into MySQL.
    """

    db = get_connection()
    cursor = db.cursor()

    query = """
    INSERT INTO interactions
    (
        doctor_name,
        hospital,
        interaction_type,
        visit_date,
        discussion,
        product,
        summary,
        notes
    )
    VALUES
    (
        %s,%s,%s,CURDATE(),%s,%s,%s,%s
    )
    """

    values = (
        "Dr. Rajesh Kumar",
        "Apollo Hospital",
        "Doctor Visit",
        details,
        "Medicine A",
        "Interaction logged through AI Assistant",
        details
    )

    cursor.execute(query, values)

    db.commit()

    cursor.close()
    db.close()

    return "✅ Interaction logged successfully."


@tool
def edit_interaction(details: str) -> str:
    """
    Edit existing HCP interaction.
    """

    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE interactions
        SET notes=%s
        ORDER BY id DESC
        LIMIT 1
        """,
        (details,)
    )

    db.commit()

    cursor.close()
    db.close()

    return "✅ Latest interaction updated successfully."


@tool
def search_interaction(doctor: str) -> str:
    """
    Search HCP interaction history.
    """

    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM interactions
        WHERE doctor_name LIKE %s
        """,
        (f"%{doctor}%",)
    )

    rows = cursor.fetchall()

    cursor.close()
    db.close()


    if not rows:
        return "No interactions found."


    response = "Previous Interactions:\n\n"

    for row in rows:

        response += f"""
Doctor: {row['doctor_name']}
Hospital: {row['hospital']}
Product: {row['product']}
Visit Date: {row['visit_date']}
Discussion: {row['discussion']}
Summary: {row['summary']}

"""

    return response



@tool
def sales_summary(_: str = "") -> str:
    """
    Generate CRM interaction summary.
    """

    db = get_connection()
    cursor = db.cursor(dictionary=True)


    cursor.execute(
        """
        SELECT 
        COUNT(*) AS total
        FROM interactions
        """
    )

    result = cursor.fetchone()


    cursor.execute(
        """
        SELECT *
        FROM interactions
        ORDER BY id DESC
        LIMIT 1
        """
    )

    latest = cursor.fetchone()


    cursor.close()
    db.close()


    if latest:

        return f"""
📊 CRM Summary

Total Interactions:
{result['total']}

Latest Visit:

Doctor:
{latest['doctor_name']}

Hospital:
{latest['hospital']}

Product:
{latest['product']}

Discussion:
{latest['discussion']}

Follow-up:
{latest['followup']}
"""

    return "No interactions available."



@tool
def followup_reminder(_: str = "") -> str:
    """
    Show upcoming follow-ups.
    """

    db = get_connection()
    cursor = db.cursor(dictionary=True)


    cursor.execute(
        """
        SELECT doctor_name, followup
        FROM interactions
        WHERE followup IS NOT NULL
        """
    )


    rows = cursor.fetchall()


    cursor.close()
    db.close()


    if not rows:
        return "No pending follow-ups."


    response = "Upcoming Follow-ups:\n"

    for row in rows:
        response += f"""
Doctor: {row['doctor_name']}
Date: {row['followup']}
"""

    return response