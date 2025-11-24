import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("SuperMarket Analysis.csv")

# Group by Branch and get total sales
branch_sales = data.groupby("Branch")["Sales"].sum()

# Pick top 2
top2 = branch_sales.sort_values(ascending=False).head(2)

# Store in x and y
x = top2.index          # Branch names
y = top2.values         # Sales values

# Plot
plt.figure(figsize=(8,5))
plt.bar(x, y, color='green')
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.title("Top 2 Branches by Sales")
plt.show()
