import plotly.express as px
import pandas as pd


def generate_chart(df: pd.DataFrame):
    """
    Automatically choose the best chart based on DataFrame columns.
    Returns a Plotly figure or None.
    """

    if df.empty:
        return None

    columns = df.columns.tolist()

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    non_numeric_cols = [
        col for col in columns
        if col not in numeric_cols
    ]

    # Date + Number -> Line Chart
    for col in columns:
        if "date" in col.lower():
            if len(numeric_cols) >= 1:
                return px.line(
                    df,
                    x=col,
                    y=numeric_cols[0],
                    title=f"{numeric_cols[0]} over {col}"
                )

    # Category + Number -> Bar Chart
    if len(non_numeric_cols) >= 1 and len(numeric_cols) >= 1:
        return px.bar(
            df,
            x=non_numeric_cols[0],
            y=numeric_cols[0],
            title=f"{numeric_cols[0]} by {non_numeric_cols[0]}"
        )

    # Two Numbers -> Scatter Plot
    if len(numeric_cols) >= 2:
        return px.scatter(
            df,
            x=numeric_cols[0],
            y=numeric_cols[1],
            title=f"{numeric_cols[1]} vs {numeric_cols[0]}"
        )

    return None