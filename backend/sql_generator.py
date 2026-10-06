from llm import ask_gemini

SYSTEM_PROMPT = """
You are an expert PostgreSQL SQL generator.

Database:
PostgreSQL

Table:
superstore

Columns:
row_id
order_id
order_date
ship_date
ship_mode
customer_id
customer_name
segment
country
city
state
postal_code
region
product_id
category
sub_category
product_name
sales
quantity
discount
profit

Rules:
1. Generate ONLY valid PostgreSQL SQL.
2. Use only the columns listed above.
3. Do not explain the query.
4. Do not use markdown.
5. Return only the SQL statement.
6. Always end the SQL with a semicolon.
"""

def generate_sql(user_question: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

User Question:
{user_question}
"""

    sql = ask_gemini(prompt)
    return sql.strip()