import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib as mpl

### Matplotlib & Seaborn
df = pd.read_csv(r'data_analysis_adv/datasets/ABNB_stock/ABNB_stock.csv')
'''df['Date'] = pd.to_datetime(df['Date'])
fig, ax = plt.subplots() 
sns.lineplot(
    data=df, x='Date', y='Close',ax=ax
)
#ax.tick_params(axis='x', labelrotation=60)
ax.xaxis.set_major_formatter(
    mpl.dates.ConciseDateFormatter(
        ax.xaxis.get_major_locator()
    )
)
plt.show()'''


### Plotly
'''fig = px.line(
    data_frame=df, x='Date', y='Close',
    width=700, height=500
)
fig.show()'''

fig = px.line(
    data_frame = df, x='Date', y='Close',
    width=700,height=500
)
fig.update_xaxes(tickformat='%Y-%m-%d')
fig.show()