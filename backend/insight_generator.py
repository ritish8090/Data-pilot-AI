import pandas as pd
from llm import ask_gemini


def generate_insights(question: str, df: pd.DataFrame) -> str:
    """
    Generate business insights from a query result.
    """

    if df.empty:
        return "No data available to analyze."

    # Limit rows so the prompt stays small
    preview = df.head(20).to_markdown(index=False)

    prompt = f"""
You are an experienced Business Analyst.

User Question:
{question}

Query Result:
{preview}

Analyze this data and provide:

1. Key Insights
2. Trends
3. Risks
4. Recommendations

Rules:
- Use bullet points.
- Keep the answer concise.
- Do not repeat the table.
- Focus on business decisions.
"""

    return ask_gemini(prompt)