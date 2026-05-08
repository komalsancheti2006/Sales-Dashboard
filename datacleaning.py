import pandas as pd
#Loading dataset
df=pd.read_csv("ecommerce_sales_data.csv")
#fill null values with 0
df=df.fillna(0)
#drop duplicates
df=df.drop_duplicates()
#Total sales
print("Total Sales:", df["Sales"].sum())
#Sales by Category
print("Sales by Category:")
print(df.groupby("Category")["Sales"].sum())
#Sales by Region
print("Sales by Region:")
print(df.groupby("Region")["Sales"].sum())
#Average Quantity by Product
print("Average Quantity by Product:")
print(df.groupby("Product Name")["Quantity"].mean().sort_values(ascending=False))
#Profit by Category
print("Profit by Category:")
print(df.groupby("Category")["Profit"].sum())
print("Profit by Region:")
region_sales=df.groupby("Region")["Profit"].sum()
print("Region with top sales:",region_sales.idxmax())
print("Region with lowest sales:",region_sales.idxmin())
#best and worst category
category_sales = df.groupby("Category")["Sales"].sum()
print("Top Category:", category_sales.idxmax())
print("Lowest Category:", category_sales.idxmin())
#new performance column
df["Performance"]=df["Profit"].apply(lambda x:"High" if x>=2000 else "Medium" if x>=1000 else "Low")
#new profit_margin column
df["Profit_Margin"]=df["Profit"]/df["Sales"]
#grouping profit margin category wise for analysis
print(df.groupby("Category")["Profit_Margin"].mean())
#saving cleaned data to another file
df.to_csv("Clean_data.csv",index=False)
