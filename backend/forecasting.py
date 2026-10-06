from database import run_query
import pandas as pd
from sklearn.linear_model import LinearRegression


def forecast_sales(days=90):

    query = """
    SELECT
        TO_DATE(order_date, 'MM/DD/YYYY') AS ds,
        SUM(sales) AS y
    FROM superstore
    GROUP BY ds
    ORDER BY ds;
    """

    df = run_query(query)

    # Ensure dates are datetime
    df["ds"] = pd.to_datetime(df["ds"])

    # Create numeric day index
    df["day"] = (df["ds"] - df["ds"].min()).dt.days

    X = df[["day"]]
    y = df["y"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Create future dates
    last_day = df["day"].max()

    future_days = pd.DataFrame({
        "day": range(last_day + 1, last_day + days + 1)
    })

    # Predict
    future_days["yhat"] = model.predict(future_days)

    # Convert day index back to dates
    future_days["ds"] = (
        df["ds"].min() +
        pd.to_timedelta(future_days["day"], unit="D")
    )

    return future_days[["ds", "yhat"]]