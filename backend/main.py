from fastapi import FastAPI
from pydantic import BaseModel
from agents.graph import graph
from langchain_core.messages import HumanMessage
from dashboard_generator import build_dashboard
from forecasting import forecast_sales
from anomaly_detection import detect_anomalies
from pdf_report import generate_pdf
from fastapi import UploadFile, File
import shutil
import os

from rag.index_builder import IndexBuilder

UPLOAD_DIR = "../uploads/documents"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

app = FastAPI(
    title="DataPilot AI API",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Welcome to DataPilot AI"
    }


@app.post("/query")
def query(request: QueryRequest):

    response = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=request.question
                )
            ]
        }
    )

    final_answer = response["messages"][-1].content

    return {
        "success": True,
        "answer": final_answer
    }

@app.get("/dashboard")
def dashboard():

    data = build_dashboard()

    return {
        "revenue":
            data["revenue"].to_dict(orient="records"),

        "profit":
            data["profit"].to_dict(orient="records"),

        "customers":
            data["customers"].to_dict(orient="records"),

        "top_products":
            data["top_products"].to_dict(orient="records"),

        "monthly_sales":
            data["monthly_sales"].to_dict(orient="records"),
        
        "region_sales":
            data["region_sales"].to_dict(orient="records")
    }

@app.get("/forecast")
def forecast():

    df = forecast_sales(90)

    return df.to_dict(orient="records")

@app.get("/anomalies")
def anomalies():

    df = detect_anomalies()

    return df.to_dict(orient="records")

@app.get("/report")
def report():

    pdf = generate_pdf(
        revenue=2300000,
        profit=286000,
        customers=793,
        insights="Revenue increased steadily across all regions.",
        forecast="Sales expected to increase by 12%.",
        recommendations="Increase investment in Technology category."
    )

    return {
        "file": pdf
    }

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    save_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(save_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    builder = IndexBuilder()

    builder.build(
        UPLOAD_DIR,
        "../vector_store"
    )

    return {
        "success": True,
        "filename": file.filename
    }