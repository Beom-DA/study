import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
import matplotlib.transforms as transforms

### 선형회귀 그래프에 선형회귀 식과 결정계수 표시하기(Matplotlib & Seaborn)

'''df = sns.load_dataset('mpg')
from scipy.stats import linregress
df = df.dropna() # 결측치가 한개라도 존재하면 밑의 코드에서 s, i ,r, p, se 의 값이 nan으로 나오기 떄문에, 결측치를 제거한다.

s, i, r, p, se = linregress(df['horsepower'], df['weight'])
# s: slope(기울기)
# i: intercept(절편)
# r : rvalue(상관계수, Pearson correalation coefficient) -1 ~ 1 사이의 값
# r**2 : 결정계수(coefficient of determination) 0에 가까우면 독립 변수가 종속 변수를 거의 설명하지 못함, 1에 가까우면 완벽하게 설명함
# p : pvalue(유의확률)
# se : stderr(표준 오차) slope의 표준오차, 즉, 추정치의 불확실성 정도
# s, i, r, _, _ = 으로 쓰면 _에 해당하는 값들은 받고 버리겠다 라는 의미

fig, ax = plt.subplots()

#★ 첫 번째 방법
# sns.regplot(
#     data=df, x='horsepower', y='weight', ax=ax,
#     line_kws={'label' : 'y={:.2f}x + {:.2f}, R^2={:.2f}'.format(s,i,r**2)}
# )
# ax.legend() # line_kws를 띄워주는 코드

#★ 두 번째 방법
sns.regplot(
    data=df, x='horsepower', y='weight', ax=ax,
    )
ax.text(
    x=0.05, y=0.9,
    s='y={:.2f}x + {:.2f}, R^2={:.2f}'.format(s,i,r**2),
    transform = ax.transAxes # 좌표에 상대좌표를 넣겠다
)

plt.show()'''




### 선형회귀 그래프에 선형회귀 식과 결정계수 표시하기(Plotly)
df = sns.load_dataset('mpg')
fig = px.scatter(
    data_frame=df, x='horsepower', y='weight',
    width=500, height=400,
    trendline='ols'
)

results = px.get_trendline_results(fig)
results = results.iloc[0]['px_fit_results']
# print(results.summary())
# print(results.params) # y절편과 기울기 값
# print(results.rsquared) # 결정계수값

fig.add_annotation(
    text='y={:.2f}x + {:.2f}, R^2={:.2f}'.format(
        results.params[1], results.params[0], results.rsquared),
        x=0.05, y=0.95, xref='x domain', yref='y domain', showarrow=False
)
fig.show()