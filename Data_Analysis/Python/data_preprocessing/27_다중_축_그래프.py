import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl


### 2개의 y축 Matplotlib & Seaborn

'''df = pd.read_csv(r'data_analysis_adv/datasets/ABNB_stock/ABNB_stock.csv')
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots()
ax2 = ax.twinx()

sns.lineplot(
    data=df, x='Date', y='Close', ax=ax, color = 'red'
)
sns.lineplot(
    data=df, x='Date', y='Volume', ax=ax2, color = 'blue'
)

ax.tick_params(axis='y', labelcolor = 'red')
ax.yaxis.label.set_color('red')

ax2.tick_params(axis='y', labelcolor='blue')
ax2.yaxis.label.set_color('blue')

ax.xaxis.set_major_formatter(
    mpl.dates.ConciseDateFormatter(
        ax.xaxis.get_major_locator()
    )
)

plt.show()'''



### 3개의 y축 Matplotlib & Seaborn
'''df = pd.read_csv(r'data_analysis_adv/datasets/ABNB_stock/ABNB_stock.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['High-Low'] = df['High'] - df['Low']

fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75) # 오른쪽 25% 공간을 비우겠다

ax2 = ax.twinx()
ax3 = ax.twinx()

ax3.spines.right.set_position(("axes", 1.2)) # 세 번째 y축을 그래프 바깥으로 옮깁니다.

sns.lineplot(data=df, x='Date', y='Close', ax=ax, color='red')
sns.lineplot(data=df, x='Date', y='Volume', ax=ax2, color='blue')
sns.lineplot(data=df, x='Date', y='High-Low', ax=ax3, color='green')

ax.yaxis.label.set_color('red')
ax2.yaxis.label.set_color('blue')
ax3.yaxis.label.set_color('green')

ax.tick_params(axis='y', labelcolor = 'red')
ax2.tick_params(axis='y', labelcolor = 'blue')
ax3.tick_params(axis='y', labelcolor = 'green')

ax.xaxis.set_major_formatter(
    mpl.dates.ConciseDateFormatter(
        ax.xaxis.get_major_locator()
    )
)

plt.show()'''



### 2개의 y축 Plotly
'''from plotly.subplots import make_subplots
df = pd.read_csv(r'data_analysis_adv/datasets/ABNB_stock/ABNB_stock.csv')

fig = make_subplots(specs=[[{'secondary_y' : True}]])

subfig1 = px.line(data_frame=df, x='Date', y='Close')
subfig1.update_traces(line_color='red')
subfig2 = px.line(data_frame=df, x='Date', y='Volume')
subfig2.update_traces(line_color='blue')

subfig2.update_traces(yaxis='y2')

fig.add_traces(subfig1.data + subfig2.data)

fig.layout.xaxis.title = 'Date'
fig.layout.yaxis.title = 'Close'
fig.layout.yaxis2.title = 'Volume'
fig.layout.yaxis.color = 'red'
fig.layout.yaxis2.color = 'blue'

fig.update_layout(width=500, height=400)
fig.show()'''



### 3개의 y축 Plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv(r'data_analysis_adv/datasets/ABNB_stock/ABNB_stock.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['High-Low'] = df['High'] - df['Low']

fig = make_subplots()
fig.add_trace(
    go.Scatter(#scatter를 쓰더라도 산점도 그래프가 만들어지지 않고 mode에 해당하는 그래프가 만들어진다
        x=df['Date'], y=df['Close'], name='Close',
        mode = 'lines', yaxis='y',
        line={'color':'red'}
    )
)
fig.add_trace(
    go.Scatter(#scatter를 쓰더라도 산점도 그래프가 만들어지지 않고 mode에 해당하는 그래프가 만들어진다
        x=df['Date'], y=df['Volume'], name='Volume',
        mode = 'lines', yaxis='y2',
        line={'color':'blue'}
    )
)
fig.add_trace(
    go.Scatter(#scatter를 쓰더라도 산점도 그래프가 만들어지지 않고 mode에 해당하는 그래프가 만들어진다
        x=df['Date'], y=df['High-Low'], name='High-Low',
        mode = 'lines', yaxis='y3',
        line={'color':'green'}
    )
)

fig.update_layout(
    yaxis = dict(title = 'Close'),
    yaxis2 = dict(
        position = 1, #상대좌표, 가장 우측에 위치
        title = 'Volume',
        side = 'right', anchor = 'free',
        overlaying = 'y'#겹쳐그릴 때 필요한 인자
    ),
    yaxis3 = dict(
        title='High-Low', side='right',
        anchor='x',# y축이 x축이랑 만난다
        overlaying='y'
    ),
    xaxis = dict(
        title='Data', domain=[.1,.85]),# x축을 0.1부터 0.85까지 쓰겠다
        width=600, height=400
    
)

fig.layout.yaxis.color = 'red'
fig.layout.yaxis2.color = 'blue'
fig.layout.yaxis3.color = 'green'

fig.show()
