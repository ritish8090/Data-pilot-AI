from sql_generator import generate_sql
from database import run_query
from insight_generator import generate_insights


def execute_question(question):

    sql = generate_sql(question)

    df = run_query(sql)

    insights = generate_insights(question, df)

    return {
        "question": question,
        "sql": sql,
        "data": df,
        "insights": insights
    }