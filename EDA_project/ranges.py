import pandas as pd 

df = pd.read_csv("Housing.csv")

print(df["price"].max() - df["price"].min())