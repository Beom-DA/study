### Heatmap(Matplotlib & Seaborn)

# pivot table
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

df = pd.read_csv(r'data_analysis_adv/datasets/medical_cost/medical_cost.csv')
age_bin_list = np.arange(10,80,10)
df['age_bin'] = pd.cut(df['age'], bins=age_bin_list)

pivot_df = df.pivot_table(
    index='age_bin', columns='region',
    values='charges', aggfunc='median'
)
#print(pivot_df)

'''fig, ax = plt.subplots()
color = sns.light_palette('seagreen', as_cmap=True)
sns.heatmap(data = pivot_df, ax=ax, annot = True, fmt='.2e',
            vmax=16000, vmin=0, cmap= color #cmap = 'RdBu')

plt.show()'''




### Heatmap(Plotly)

fig = px.imshow(
    pivot_df, x = pivot_df.columns, y = pivot_df.index.astype('str'),
    text_auto='.2e', width=400, height=400,
    color_continuous_scale='RdBu'
)
fig.show()



