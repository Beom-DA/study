### axes-level plot을 특정 변수의 그룹별로 subplot으로 나눠 그리기

# ax를 리스트 형식으로 지정하여 plot

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

df = pd.read_csv(r'data_analysis_adv/datasets/medical_cost/medical_cost.csv')

fig, ax = plt.subplots(2, 2, figsize = (12,12))

'''sns.regplot(x = 'bmi', y = 'charges', data = df.query('region == "southwest"'),
            ax=ax[0][0])
ax[0][0].set_title('region : southwest')

sns.regplot(x = 'bmi', y = 'charges', data = df.query('region == "southeast"'),
            ax=ax[0][1])
ax[0][1].set_title('region : southeast')

sns.regplot(x = 'bmi', y = 'charges', data = df.query('region == "northwest"'),
            ax=ax[1][0])
ax[1][0].set_title('region : northwest')

sns.regplot(x = 'bmi', y = 'charges', data = df.query('region == "northeast"'),
            ax=ax[1][1])
ax[1][1].set_title('region : northeast')

plt.show()
'''


### igure-level plot을 특정 변수의 그룹별로 subplot으로 나눠 그리기
# row, col, col_wrap 인자 사용

'''sns.lmplot(
    x='bmi', y='charges', data=df,
    col='region', col_wrap=2,# col_wrap은 몇 열까지 만들거냐
    sharex=False, sharey=False, # 공통된 x, y를 사용할거냐

)'''
'''sns.lmplot(
    x='bmi', y='charges', data=df,
    col='region', row = 'smoker', hue='sex',
    sharex=False, sharey=False,
    
)
plt.show()'''


###axes-leve plot을 figure_level plot처럼 그리기
'''g = sns.FacetGrid(
    data = df, col='region', col_wrap=2,
    sharex=False, sharey=False
)
g.map_dataframe(
    sns.boxenplot, x = 'smoker', y = 'charges', hue = 'sex'
)
plt.show()'''




### Plotly express 함수들의 facet 사용
fig = px.scatter(
    data_frame=df, x='bmi', y='charges',
    color='sex', facet_row='region', facet_col='smoker',
    width=700, height=1200, trendline='ols',# trendline은 선형회귀선을 의미하고, ols는 Ordinary Least Squares (최소제곱법)을 의미한다.
    facet_col_spacing=0.05 # 그래프 사이의 공간 설정
).update_yaxes(matches=None, showticklabels=True) #seaborn에서 shareY와 같은 기능.
fig.show()

