import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'data_analysis_adv/datasets/ABNB_stock/ABNB_stock.csv')

fig, ax = plt.subplots() 
sns.lineplot(
    data=df, x='Date', y='Close',ax=ax
)
plt.show()