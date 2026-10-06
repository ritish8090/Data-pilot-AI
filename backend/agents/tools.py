from langchain.tools import tool

from query_executor import execute_question
from forecasting import forecast_sales
from anomaly_detection import detect_anomalies
from rag.rag_chain import RAGChain

rag = RAGChain()


@tool
def sql_tool(question: str) -> str:
    """Answer questions about sales, profit, customers, products, orders and regions."""

    result = execute_question(question)

    if "error" in result:
        return result["error"]

    return str(result["data"])


@tool
def rag_tool(question: str) -> str:
    """Answer questions using uploaded PDF or DOCX documents."""

    result = rag.ask(question)

    return result["answer"]


@tool
def forecast_tool(question: str = "") -> str:
    """Forecast future sales."""

    df = forecast_sales(90)

    return df.to_string()


@tool
def anomaly_tool(question: str = "") -> str:
    """Detect anomalies in the dataset."""

    df = detect_anomalies()

    return df.to_string()