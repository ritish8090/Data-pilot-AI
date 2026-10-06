import streamlit as st
import requests
import pandas as pd
from chart_generator import generate_chart
import plotly.express as px
import plotly.graph_objects as go
import os

# -----------------------------
# Create reports/charts folder
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REPORT_DIR = os.path.join(
    BASE_DIR,
    "..",
    "reports",
    "charts"
)

os.makedirs(REPORT_DIR, exist_ok=True)

API_URL = "http://127.0.0.1:8000/query"
UPLOAD_URL = "http://127.0.0.1:8000/upload"

st.set_page_config(
    page_title="DataPilot AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 DataPilot AI")
st.write("Ask questions about your Superstore dataset using natural language.")
st.divider()

st.subheader("📂 Upload Documents")
uploaded_file = st.file_uploader(
    "Upload PDF, DOCX, TXT or CSV",
    type=["pdf", "docx", "txt", "csv"]
)
if uploaded_file is not None:

    if st.button("Upload Document"):

        with st.spinner("Uploading and building vector database..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue()
                )
            }

            response = requests.post(
                UPLOAD_URL,
                files=files
            )

        if response.status_code == 200:

            st.success("Document uploaded successfully!")

        else:

            st.error(response.text)

st.divider()

st.subheader("🤖 AI Business Copilot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

prompt = st.chat_input(
    "Ask anything about your business..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = requests.post(
        API_URL,
        json={
            "question": prompt
        }
    )

    answer = response.json()["answer"]

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# ---------------- Dashboard Button ---------------- #

if st.button("📊 Build Executive Dashboard"):

    response = requests.get("http://127.0.0.1:8000/dashboard")

    dashboard = response.json()

    st.success("Executive Dashboard Generated")

       # KPIs

    col1, col2, col3 = st.columns(3)

    with col1:
       st.metric(
           "Revenue",
           f"${dashboard['revenue'][0]['revenue']:,.2f}"
        )

    with col2:
       st.metric(
           "Profit",
           f"${dashboard['profit'][0]['profit']:,.2f}"
        )

    with col3:
       st.metric(
           "Customers",
           dashboard["customers"][0]["customers"]
        )

 # ---------------- Top Products ---------------- #
    st.subheader("🏆 Top Products")

    df_products = pd.DataFrame(
        dashboard["top_products"]
   )

    fig_products = px.bar(
        df_products,
        x="sales",
        y="product_name",
        orientation="h",
        title="Top 10 Products by Sales"
    )

    st.plotly_chart(fig_products, use_container_width=True)
    fig_products.write_image(os.path.join(REPORT_DIR, "top_products.png"))
 # ---------------- Monthly Trend ---------------- #
    st.subheader("📈 Monthly Sales Trend")

    df_month = pd.DataFrame(
        dashboard["monthly_sales"]
    )

    fig_month = px.line(
        df_month,
        x="month",
        y="sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    st.plotly_chart(fig_month, use_container_width=True)
    fig_month.write_image(os.path.join(REPORT_DIR, "monthly_sales.png"))
 # ---------------- Region ---------------- #
    st.subheader("🌍 Revenue by Region")

    df_region = pd.DataFrame(
        dashboard["region_sales"]
    )

    fig_region = px.bar(
        df_region,
        x="region",
        y="revenue",
        title="Revenue by Region"
   )

    st.plotly_chart(fig_region, use_container_width=True)
    fig_region.write_image(os.path.join(REPORT_DIR, "region_sales.png"))
# ---------------- Question Box ---------------- #

# question = st.text_input(
#     "Ask a question",
#     placeholder="Example: Top 5 customers by revenue"
# )

# if st.button("Submit"):

#     if question.strip() == "":
#         st.warning("Please enter a question.")
#         st.stop()

#     with st.spinner("Generating SQL and fetching data..."):

#         response = requests.post(
#             API_URL,
#             json={"question": question}
#         )

#     if response.status_code != 200:
#         st.error("Backend server error.")
#         st.stop()

#     result = response.json()

#     if not result.get("success", False):
#         st.error(result.get("error", "Unknown error"))

#         if "sql" in result:
#             st.subheader("Generated SQL")
#             st.code(result["sql"], language="sql")

#         st.stop()

#     # ---------------- SQL ---------------- #

#     st.subheader("Generated SQL")
#     st.code(result["sql"], language="sql")

#     # ---------------- TABLE ---------------- #

#     df = pd.DataFrame(result["data"])

#     st.subheader("Results")
#     st.dataframe(df, use_container_width=True)

#     # ---------------- CHART ---------------- #

#     fig = generate_chart(df)

#     if fig is not None:
#         st.subheader("Visualization")
#         st.plotly_chart(fig, use_container_width=True)

#     # ---------------- AI INSIGHTS ---------------- #

#     st.subheader("🤖 AI Insights")

#     if "insights" in result:
#         st.markdown(result["insights"])
#     else:
#         st.info("No insights available.")

st.divider()

if st.button("📈 Predict Next 3 Months Sales"):

    response = requests.get(
        "http://127.0.0.1:8000/forecast"
    )

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    forecast = pd.DataFrame(response.json())

    st.subheader("📈 Sales Forecast")

    fig = px.line(
        forecast,
        x="ds",
        y="yhat",
        markers=True,
        title="Predicted Sales (Next 3 Months)"
    )

    st.plotly_chart(fig, use_container_width=True)
    fig.write_image(os.path.join(REPORT_DIR, "forecast.png"))

    predicted_revenue = forecast["yhat"].sum()

    st.metric(
        "Predicted Revenue",
        f"${predicted_revenue:,.2f}"
    )

st.divider()

if st.button("🚨 Detect Sales Anomalies"):

    with st.spinner("Finding unusual transactions..."):

        response = requests.get(
            "http://127.0.0.1:8000/anomalies"
        )

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    anomalies = pd.DataFrame(response.json())

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Anomalies Detected",
            len(anomalies)
        )

    with col2:
        st.metric(
            "Highest Sale",
            f"${anomalies['sales'].max():,.2f}"
        )

    with col3:
        st.metric(
            "Lowest Profit",
            f"${anomalies['profit'].min():,.2f}"
        )

    st.subheader("🚨 Anomalous Transactions")
    st.dataframe(
        anomalies,
        use_container_width=True
    ) 

    fig = px.scatter(
        anomalies,
        x="sales",
        y="profit",
        color="region",
        hover_data=[
            "customer_name",
            "category"
        ],
        title="Sales vs Profit (Detected Anomalies)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    fig.write_image(os.path.join(REPORT_DIR, "anomalies.png"))

st.divider()

if st.button("📄 Generate Executive Report"):

    response = requests.get(
        "http://127.0.0.1:8000/report"
    )

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    result = response.json()

    st.success(
        f"PDF Generated: {result['file']}"
    )
   