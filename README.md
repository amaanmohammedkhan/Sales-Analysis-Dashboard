# Sales Data Analysis Dashboard

<img width="1382" height="773" alt="image" src="https://github.com/user-attachments/assets/9fcec9d6-2e8e-4303-b684-61f5a9815f33" />



**Developer:** Amaan Mohammed Khan

An end-to-end sales analytics project: raw retail data is cleaned with Python, loaded into a MySQL database, analyzed with SQL, and visualized in an interactive Power BI dashboard connected live to the database.

## Overview

This project simulates a real-world analyst workflow — starting from a raw CSV export and ending in a live, interactive dashboard, rather than just producing a static chart from a spreadsheet.

**Pipeline:** CSV → Python (clean) → MySQL (store & query) → SQL (analyze) → Power BI (visualize)

## Tech Stack

- **Python** (pandas) — data cleaning and transformation
- **SQLAlchemy + PyMySQL** — loading data from Python into MySQL
- **MySQL** — relational database for storing and querying data
- **Power BI** — live-connected interactive dashboard

## Dataset

[Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) (Kaggle) — ~9,994 retail order line items from 2014–2017, covering orders, customers, products, regions, sales, and profit.

## Project Structure

```
sales_project/
│
├── Sample - Superstore.csv     # Raw dataset
├── load_data.py                 # Loads raw CSV into MySQL ('orders' table)
├── clean_data.py                 # Cleans data, adds Order Month, saves to MySQL ('cleaned_orders' table)
├── queries.sql                   # All SQL analysis queries
├── Sales_Dashboard.pbix          # Power BI dashboard file
└── README.md
```

## What Was Done

### 1. Data Loading (`load_data.py`)
Read the raw CSV with pandas, handled a `UnicodeDecodeError` from the Excel-exported file by specifying `latin1` encoding, and loaded the raw data into MySQL as an `orders` table using SQLAlchemy.

### 2. Data Cleaning (`clean_data.py`)
- Checked for missing values and duplicate rows (found none — the dataset was already clean)
- Converted `Order Date` from text to a proper date type
- Added an `Order Month` column for time-based grouping
- Saved the cleaned data into MySQL as a separate `cleaned_orders` table, keeping the raw data untouched

### 3. SQL Analysis (`queries.sql`)
Wrote queries to calculate:
- Total revenue
- Average order value (both a simple average and a precise version using a subquery that groups by `Order ID` first)
- Revenue by category
- Revenue by month

### 4. Power BI Dashboard
Connected Power BI directly to the live MySQL database (not a static file import) and built:
- KPI cards for Total Revenue, Average Order Value, and Total Orders
- A monthly revenue trend line chart
- A revenue-by-category bar chart
- An interactive date-range slicer

## Key Findings

| Metric | Value |
|---|---|
| Total Revenue | ≈ $2,297,200.86 |
| Avg. Order Value (per line item) | ≈ $229.86 |
| Avg. Order Value (per actual order) | ≈ $458.61 |
| Total Unique Orders | ≈ 5,009 |
| Top Revenue Category | Technology (≈ $836,154) |
| Strongest Months | November & December (holiday seasonality) |
| Weakest Months | January & February |
| Strongest Year | 2017 |

**Notable insight:** The naive average order value (per line item) was $229.86, but grouping by actual `Order ID` first — since one order can contain multiple products — gave a true AOV of $458.61, nearly double. This showed most customers buy multiple items per order.

Revenue also showed clear holiday seasonality: November and December were consistently the strongest months every year, while January and February were consistently the weakest, with an overall upward trend peaking in 2017.

## How to Run This Project

1. Install dependencies: `pip install pandas sqlalchemy pymysql`
2. Set up a local MySQL database named `sales_project`
3. Run `python load_data.py` to load the raw data
4. Run `python clean_data.py` to clean the data and save it to MySQL
5. Run the queries in `queries.sql` in MySQL Workbench to reproduce the analysis
6. Open `Sales_Dashboard.pbix` in Power BI Desktop and update the MySQL connection credentials to view the dashboard

## Developer

**Amaan Mohammed Khan**
Final-year B.Tech student, Computer Science (Data Science)
