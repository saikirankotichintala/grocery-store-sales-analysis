# 🛒 Grocery Store Analytics Dashboard

A clean and interactive **analytics dashboard** built using **Python, Dash, Plotly, and MySQL** to analyze grocery store sales and inventory data.

This project focuses on **visual storytelling**, turning raw database data into meaningful business insights.

---

## ✨ What This Project Does

- Shows **monthly sales trends**
- Identifies **top-selling products**
- Visualizes **sales distribution**
- Analyzes **stock vs price relationship**
- Uses a **dark, professional UI**

---

## 🧰 Tech Used

- Python  
- Dash  
- Plotly  
- Pandas  
- MySQL  
- SQLAlchemy  
- PyMySQL  

---

## 📊 Visualizations Included

- 📅 Monthly Sales Bar Chart  
- 🏆 Top 10 Products by Sales  
- 🧁 Sales Distribution Pie Chart  
- 📦 Stock vs Price Scatter Plot  

All charts are generated **directly from a MySQL database**.

---

## 📸 Dashboard Screenshots

### 📅 Monthly Sales Overview (Bar Chart)
![Monthly Sales Overview](screenshots/Montly_sales_overview(bar%20chart).png)

### 🧁 Sales Distribution (Pie Chart)
![Sales Distribution](screenshots/Sales_Distribution(Pie%20Chart).png)

### 📦 Stock vs Price (Scatter Plot)
![Stock vs Price](screenshots/Stock_vs_Price_(scatter%20plot).png)

### 🏆 Top 10 Products by Sales (Bar Chart)
![Top 10 Products](screenshots/Top_10_Products_by_sales(bar%20chart).png)

---

## 📁 Project Structure
Grocery-Store-Analytics/
├── app.py
├── products_10000_with_nulls.csv
├── sales_10000_with_nulls.csv
├── screenshots/
├── requirements.txt
└── README.md

---

## ▶️ How to Run

1. Make sure MySQL is running  
2. Update database credentials in `app.py`  
3. Run the application:

```bash
python app.py

## Open in browser:

http://127.0.0.1:8050
