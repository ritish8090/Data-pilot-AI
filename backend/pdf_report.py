from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image

def generate_pdf(
        revenue,
        profit,
        customers,
        insights,
        forecast,
        recommendations):

    pdf = SimpleDocTemplate("Executive_Report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>DataPilot AI Executive Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph(f"Revenue : ${revenue:,.2f}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Profit : ${profit:,.2f}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Customers : {customers}", styles["BodyText"])
    )

    elements.append(
        Paragraph("<b>AI Insights</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(insights, styles["BodyText"])
    )

    elements.append(
        Paragraph("<b>Forecast</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(forecast, styles["BodyText"])
    )

    elements.append(
        Paragraph("<b>Recommendations</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(recommendations, styles["BodyText"])
    )
    
    elements.append(
        Paragraph("Top Products", styles["Heading2"])
    )

    elements.append(
        Image(
            "reports/charts/top_products.png",
            width=450,
            height=250
        )
    )

    elements.append(
        Paragraph("Monthly Sales Trend", styles["Heading2"])
    )

    elements.append(
        Image(
            "reports/charts/monthly_sales.png",
            width=450,
            height=250
        )
    )

    elements.append(
        Paragraph("Revenue by Region", styles["Heading2"])
    ) 

    elements.append(
        Image(
            "reports/charts/region_sales.png",
            width=450,
            height=250
        )
    )

    elements.append(
        Paragraph("Sales Forecast", styles["Heading2"])
    )

    elements.append(
        Image(
            "reports/charts/forecast.png",
            width=450,
            height=250
        )
    )

    elements.append(
        Paragraph("Anomaly Detection", styles["Heading2"])
    )

    elements.append(
        Image(
            "reports/charts/anomalies.png",
            width=450,
            height=250
        )
    )
    pdf = SimpleDocTemplate(
        "reports/Executive_Report.pdf"
    )

    return "reports/Executive_Report.pdf"