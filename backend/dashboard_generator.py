from database import run_query

def build_dashboard():

    revenue = run_query("""
        SELECT SUM(sales) AS revenue
        FROM superstore;
    """)

    profit = run_query("""
        SELECT SUM(profit) AS profit
        FROM superstore;
    """)

    customers = run_query("""
        SELECT COUNT(DISTINCT customer_name) AS customers
        FROM superstore;
    """)

    top_products = run_query("""
        SELECT
            product_name,
            SUM(sales) AS sales
        FROM superstore
        GROUP BY product_name
        ORDER BY sales DESC
        LIMIT 10;
    """)

    monthly_sales = run_query("""
        SELECT
            DATE_TRUNC('month', TO_DATE(order_date, 'MM/DD/YYYY')) AS month,
            SUM(sales) AS sales
        FROM superstore
        GROUP BY DATE_TRUNC('month', TO_DATE(order_date, 'MM/DD/YYYY'))
        ORDER BY DATE_TRUNC('month', TO_DATE(order_date, 'MM/DD/YYYY'));
    """)

    region_sales = run_query("""
        SELECT
            region,
            SUM(sales) AS revenue
       FROM superstore
       GROUP BY region
       ORDER BY revenue DESC;
    """)

    return {
        "revenue": revenue,
        "profit": profit,
        "customers": customers,
        "top_products": top_products,
        "monthly_sales": monthly_sales,
        "region_sales": region_sales
    }