from database import run_query
from sklearn.ensemble import IsolationForest
import pandas as pd


def detect_anomalies():

    query = """
    SELECT
        order_id,
        order_date,
        customer_name,
        region,
        category,
        sales,
        profit,
        discount
    FROM superstore;
    """

    df = run_query(query)

    # Features used by Isolation Forest
    features = df[["sales", "profit", "discount"]]

    model = IsolationForest(
        contamination=0.02,
        random_state=42
    )

    df["anomaly"] = model.fit_predict(features)

    # -1 = anomaly
    anomalies = df[df["anomaly"] == -1]

    return anomalies