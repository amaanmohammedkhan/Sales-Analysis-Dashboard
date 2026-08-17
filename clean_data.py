import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# check for missing values
print(df.isnull().sum())

# check for duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# check current data type of Order Date
print(df["Order Date"].dtype)

# convert Order Date from text to an actual date type
df["Order Date"] = pd.to_datetime(df["Order Date"])

# create a new column for order month (useful for monthly trend analysis)
df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)

# confirm the change worked
print(df["Order Date"].dtype)
print(df[["Order Date", "Order Month"]].head())

# save cleaned data to MySQL
engine = create_engine("mysql+pymysql://root:1811@localhost/sales_project")
df.to_sql("cleaned_orders", engine, if_exists="replace", index=False)
print("Cleaned data saved to MySQL as 'cleaned_orders'")