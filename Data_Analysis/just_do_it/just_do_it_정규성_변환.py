import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform
import plotly.graph_objects as go
from scipy.stats import norm
from scipy.stats import probplot
from scipy.stats import stats
from scipy.stats import boxcox
from just_do_it_데이터_병합 import df


### 금액
## 히스토그램 및 정규분포 곡선
# mean_data = df['금액'].mean()
# min_data = df['금액'].min()
# max_data = df['금액'].max()
# std = df['금액'].std()
# x_curve = np.linspace(min_data, max_data, 100)
# y_curve = norm.pdf(x_curve, mean_data, std)
# # norm.pdf() --> 평균과 표준편차 기반 정규분포 곡선 생성
# fig = px.histogram(
#     data_frame=df, x='금액',width=500, height=500,
#     title='Histogram with Normal Distribution Curve',
#     nbins=100, opacity=0.6, histnorm='probability density'
#     # histnorm = 'probability density' --> 곡선과 맞추기 위해 히스토그램을 확률밀도로 정규화
# )
# fig.add_trace(
#     go.Scatter(
#         x=x_curve,
#         y=y_curve,
#         mode='lines',
#         name='Normal Distribution',
#         line=dict(color='red')
#     )
# )
# fig.show()

## Q-Q plot 생성
# fig, ax = plt.subplots()
# probplot(df['금액'], dist='norm', plot=plt)
# skewness = stats.skew(df['금액'])
# str = f'Skewness : {skewness:.3f}'
# plt.text(
#     0.05, 0.95, str,
#     transform=ax.transAxes,
#     bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray')
# )
# plt.title("Q-Q plot (Normal Distribution)")
# plt.grid(True)
# plt.show()

## box-cox 변환
boxcox_data, fitted_lambda = boxcox(df['금액'])

fig, ax = plt.subplots(1,2, figsize=(12,5))
sns.histplot(
    data=df['금액'], ax=ax[0], kde=True
)
ax[0].set_title('Before Box-cox')

sns.histplot(
    data=boxcox_data, ax=ax[1], kde=True
)
ax[1].set_title('After Box-cox')
plt.show()

print('lambda : ',fitted_lambda)
