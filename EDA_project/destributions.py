import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("Housing.csv")

df["price"].hist()

plt.show()
