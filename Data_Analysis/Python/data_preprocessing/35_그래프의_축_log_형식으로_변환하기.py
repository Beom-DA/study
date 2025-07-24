import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
import matplotlib.transforms as transforms

### 그래프의 축 log 형식으로 변환하기(Matplotlib & Seaborn)
# df = pd.read_csv(r'data_analysis_adv/datasets/Covid19-India/Covid19-India.csv')
# df['date'] = pd.to_datetime(df['date'])
# print(df)
# df = df.loc[df.region == 'Maharashtra']

# fig, ax = plt.subplots()
# sns.lineplot(
#     data=df, x='date', y='confirmed', ax=ax
# )
# ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
# ax.set_yscale('log')
# plt.show()


### 그래프의 축 log 형식으로 변환하기(Plotly)
df = pd.read_csv(r'data_analysis_adv/datasets/Covid19-India/Covid19-India.csv')
df = df.query('region == "Maharashtra"')
fig = px.line(
    data_frame=df, x='date', y='confirmed',
    width=500, height=500,
    log_y=True
)
fig.show()