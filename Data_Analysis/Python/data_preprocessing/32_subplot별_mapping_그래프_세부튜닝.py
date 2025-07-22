import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl

### 수평선, 수직선을 통해 기준선 표현하기(Matplotlib & Seaborn)
'''df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])

df = df.query('inspection_step == "A"')
fig, ax = plt.subplots()

sns.scatterplot(
    data=df, x='date', y='value', ax=ax
)
ax.xaxis.set_major_formatter(
    mpl.dates.ConciseDateFormatter(
        ax.xaxis.get_major_locator()
    )
)

ax.axhline(df['lower_spec'].iloc[-1], color='red', linewidth = 0.5)
ax.axhline(df['target'].iloc[-1], color='red', linewidth = 0.5)
ax.axhline(df['upper_spec'].iloc[-1], color='red', linewidth = 0.5)

plt.show()'''

### 수평선, 수직선을 통해 기준선 표현하기(Plotly)
df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')

fig = px.scatter(
    data_frame=df, x='date', y='value', width=500, height=500
)
fig.add_hline(df['lower_spec'].iloc[-1], line_color='red', line_width = 0.5)
fig.add_hline(df['target'].iloc[-1], line_color='red', line_width = 0.5)
fig.add_hline(df['upper_spec'].iloc[-1], line_color='red', line_width = 0.5)
fig.show()