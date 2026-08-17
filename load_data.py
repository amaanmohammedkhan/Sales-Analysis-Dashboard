import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
print(df.head())
print(df.columns.tolist())

engine = create_engine("mysql+pymysql://root:1811@localhost/sales_project")

df.to_sql("orders", engine, if_exists="replace", index=False)

print("Data loaded into MySQL successfully!")