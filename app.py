import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ---------------- DATABASE CONNECTION ----------------
engine = create_engine(
    "mysql+pymysql://root:Saikiran%4012345%24@localhost/GROCERY_STORE"
)

# ---------------- LOAD DATA ----------------
sales_df = pd.read_sql("""
    SELECT sale_date, total_amount
    FROM sales
    WHERE sale_date IS NOT NULL
""", engine)

top_products_df = pd.read_sql("""
    SELECT p.product_name, SUM(s.total_amount) AS total_sales
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_sales DESC
    LIMIT 10
""", engine)

products_df = pd.read_sql("""
    SELECT product_name, price, stock
    FROM products
    WHERE price IS NOT NULL AND stock IS NOT NULL
    LIMIT 100
""", engine)

# ---------------- GRAPHS  ----------------

sales_df["month"] = pd.to_datetime(sales_df["sale_date"]).dt.to_period("M").astype(str)

monthly_sales = sales_df.groupby("month")["total_amount"].sum().reset_index()

monthly_sales_bar = px.bar(
    monthly_sales,
    x="month",
    y="total_amount",
    title="Monthly Sales Overview",
    template="plotly_dark"
)

monthly_sales_bar.update_traces(marker_color="orange")
monthly_sales_bar.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    xaxis_title="Month",
    yaxis_title="Total Sales"
)
top_products_bar = px.bar(
    top_products_df,
    x="product_name",
    y="total_sales",
    title="Top 10 Products by Sales",
    template="plotly_dark"
)
top_products_bar.update_traces(marker_color="yellow")
top_products_bar.update_layout(plot_bgcolor="black", paper_bgcolor="black")

sales_pie = px.pie(
    top_products_df,
    names="product_name",
    values="total_sales",
    title="Sales Distribution (Top Products)",
    template="plotly_dark",
    color_discrete_sequence=px.colors.sequential.Plasma
)
sales_pie.update_layout(plot_bgcolor="black", paper_bgcolor="black")

stock_price_scatter = px.scatter(
    products_df,
    x="price",
    y="stock",
    title="Stock vs Price",
    template="plotly_dark"
)
stock_price_scatter.update_traces(
    marker=dict(color="purple", size=9, opacity=0.7)
)
stock_price_scatter.update_layout(plot_bgcolor="black", paper_bgcolor="black")

# ---------------- DASH APP ----------------
app = dash.Dash(__name__)

app.layout = html.H1("GROCERY STORE DASHBOARD", style={"textAlign": "center", "color": "white", "backgroundColor": "black", "padding": "20px"}) and html.Div(
    style={
        "backgroundColor": "black",
        "color": "white",
        "padding": "25px",
        "fontFamily": "Segoe UI, Arial"
    },
    children=[

        html.H3("📅 How are sales performing month by month?"),
        html.P(
            "This view smooths daily fluctuations and highlights overall monthly performance.",
            style={"color": "grey"}
        ),
        dcc.Graph(figure=monthly_sales_bar),

        html.Div(
            style={"display": "flex", "gap": "25px", "marginTop": "30px"},
            children=[
                html.Div(dcc.Graph(figure=top_products_bar), style={"flex": 1}),
                html.Div(dcc.Graph(figure=sales_pie), style={"flex": 1})
            ]
        ),

        html.Div(
            style={"marginTop": "25px"},
            children=[
                dcc.Graph(figure=stock_price_scatter)
            ]
        )
    ]
)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
