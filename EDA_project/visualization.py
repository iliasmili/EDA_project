import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("Housing.csv")

plt.scatter(df["area"],df["price"])
plt.xlabel("area")
plt.ylabel("price")
plt.show()
