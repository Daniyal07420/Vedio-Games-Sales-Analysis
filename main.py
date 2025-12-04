import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
data = pd.read_csv("c:\\Users\\Lenovo\\Desktop\\video_games_sales.csv")
df = pd.DataFrame(data)
print(df.head())


# Basic Data Overview
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Data Cleaning
df = df.dropna(subset=["Global_Sales"])
df["Year"] = pd.to_datetime(df["Year"], errors="coerce").dt.year
df = df.dropna(subset=["Year"])
df["Year"] = df["Year"].astype(int)
print(df.info())

# Top-Level Sales Analysis

plt.figure(figsize=(12, 6))
global_sales_trend = df.groupby("Year")["Global_Sales"].sum().reset_index()
sns.lineplot(data = global_sales_trend, x="Year", y="Global_Sales")
plt.title("Global Sales Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Global Sales")
plt.grid()
plt.show()


# Top Selling Platforms


plt.figure(figsize=(12, 6))
Platform = df.groupby("Platform")["Global_Sales"].sum().reset_index().sort_values(by="Global_Sales", ascending=False).head(10)
sns.barplot(data=Platform, x="Platform", y="Global_Sales", palette="GnBu_d")
plt.title("Top 10 Selling Platforms")
plt.xlabel("Platform")
plt.ylabel("Global Sales")
plt.xticks(rotation=45)
plt.show()


# Region-wise Genre Popularity

regions = ["NA_Sales", "EU_Sales", "JP_Sales"]
for region in regions:
    plt.figure(figsize=(12, 6))
    genre_sales = df.groupby("Genre")[region].sum().reset_index().sort_values(by=region, ascending=False).head(10)
    sns.barplot(data=genre_sales, x="Genre", y=region, palette="GnBu_d")
    plt.title(f"Top 10 Genres in {region.split('_')[0]}")
    plt.xlabel("Genre")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()


# One publisher ka total revenue


top_publishers = df.groupby("Publisher")["Global_Sales"].sum().reset_index().sort_values(by="Global_Sales", ascending=False).head(10)
plt.figure(figsize=(10, 10))
plt.pie(top_publishers["Global_Sales"], labels=top_publishers["Publisher"], autopct="%1.1f%%", startangle=40)
plt.title("Top 10 Publishers by Global Sales")
plt.show()


# Region Comparison
plt.figure(figsize=(12, 6))
region_sales = df[["NA_Sales", "EU_Sales", "JP_Sales"]].sum().reset_index()
region_sales.columns = ["Region", "Total_Sales"]
plt.figure(figsize=(8, 6))
sns.barplot(data=region_sales, x="Region", y="Total_Sales", palette="GnBu_d")
plt.title("Region-wise Total Sales Comparison")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# Correlation Analysis
plt.figure(figsize=(10, 8))
correlation_matrix = df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix of Sales Data")
plt.show()


# Worldwide Revenue According to Games


plt.figure(figsize=(12, 6))
top_games = df.groupby("Name")["Global_Sales"].sum().reset_index().sort_values(by="Global_Sales", ascending=False).head(10)
sns.barplot(data=top_games, x="Name", y="Global_Sales", palette="GnBu_d")
plt.title("Top 10 Highest Selling Video Games")
plt.xlabel("Game Name")
plt.ylabel("Global Sales")
plt.xticks(rotation=45)
plt.show()


# Sales Distribution by Genre
plt.figure(figsize=(12, 6))
genre_sales_dist = df.groupby("Genre")["Global_Sales"].sum().reset_index().sort_values(by="Global_Sales", ascending=False)
sns.barplot(data=genre_sales_dist, x="Genre", y="Global_Sales", palette="GnBu_d")
plt.title("Sales Distribution by Genre")
plt.xlabel("Genre")
plt.ylabel("Global Sales")
plt.xticks(rotation=45)
plt.show()


# Platform Popularity Over Time
plt.figure(figsize=(12, 6))
platform_trend = df.groupby(["Year", "Platform"])["Global_Sales"].sum().reset_index()
sns.lineplot(data=platform_trend, x="Year", y="Global_Sales", hue="Platform")
plt.title("Platform Popularity Over Time")
plt.xlabel("Year")
plt.ylabel("Global Sales")
plt.show()


# Publisher Performance Over Years
plt.figure(figsize=(12, 6))
publisher_trend = df.groupby(["Year", "Publisher"])["Global_Sales"].sum().reset_index()
sns.lineplot(data=publisher_trend, x="Year", y="Global_Sales", hue="Publisher")
plt.title("Publisher Performance Over Years")
plt.xlabel("Year")
plt.ylabel("Global Sales")
plt.show()

# Regional Sales Distribution
plt.figure(figsize=(12, 6))
region_sales_dist = df.melt(id_vars=["Name"], value_name="Sales", var_name="Region", value_vars=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])
sns.boxplot(data=region_sales_dist, x="Region", y="Sales", palette="GnBu_d")
plt.title("Regional Sales Distribution")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# Yearly Sales Growth Rate
df["Previous_Year_Sales"] = df.groupby("Name")["Global_Sales"].shift(1)
df["Sales_Growth_Rate"] = (df["Global_Sales"] - df["Previous_Year_Sales"]) / df["Previous_Year_Sales"] * 100
plt.figure(figsize=(12, 6))
sales_growth = df.groupby("Year")["Sales_Growth_Rate"].mean().reset_index()
sns.lineplot(data=sales_growth, x="Year", y="Sales_Growth_Rate")
plt.title("Yearly Sales Growth Rate")
plt.xlabel("Year")
plt.ylabel("Average Sales Growth Rate (%)")
plt.show()

# Save cleaned data
df.to_csv("cleaned_vedio_games_sales.csv", index=False)
print("Cleaned data saved to 'cleaned_vedio_games_sales.csv'")