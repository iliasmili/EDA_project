import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 

df = pd.read_csv("Housing.csv")

corr = df.corr(numeric_only=True)
sns.heatmap(corr , annot=True)
plt.show()
