import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("SuperMarket Analysis.csv")

plt.figure(figsize=(8,5))
plt.hist(data["Rating"], bins=6, edgecolor='black')
plt.xlabel("Rating")
plt.ylabel("Count")
plt.title("Rating Histogram")
plt.show()
