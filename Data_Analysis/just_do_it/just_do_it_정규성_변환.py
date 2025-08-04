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
from scipy.stats import skew
from just_do_it_데이터_병합 import df


if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'

plt.rcParams['axes.unicode_minus'] = False



############## 금액 ################

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
# boxcox_data, fitted_lambda = boxcox(df['금액'])

# fig, ax = plt.subplots(1,2, figsize=(12,5))
# sns.histplot(
#     data=df['금액'], ax=ax[0], kde=True # kde=True --> 곡선 그래프 첨가
# )
# ax[0].set_title('Before Box-cox')

# sns.histplot(
#     data=boxcox_data, ax=ax[1], kde=True
# )
# ax[1].set_title('After Box-cox')
# plt.show()

# print('lambda : ',fitted_lambda)


## Log 변환
df['log_금액'] = np.log(df['금액'])
# skewness = stats.skew(df['log_금액'])
#str = f'skewness : {skewness:.3f}'
# fig, ax = plt.subplots()
# sns.histplot(
#     data=df, x='log_금액', kde=True, ax=ax
# )
# plt.text(
#     0.75, 0.95, str,
#     transform = ax.transAxes
# )
# plt.show()


## Quantile 변환
# from sklearn.preprocessing import QuantileTransformer
# # series를 2d 배열로 변환
# x = df['금액'].values.reshape(-1,1)
# # 분위수 변환기 정의
# qt = QuantileTransformer(output_distribution='normal', random_state=0)
# # 변환 수행
# X_transformed = qt.fit_transform(x)
# # 다시 1차원 Series로 변환
# S_transformed = pd.Series(X_transformed.flatten(), index=df['금액'].index)

# skewness =  stats.skew(S_transformed)
# str = f'skewness : {skewness:.2f}'

# fig, ax = plt.subplots()
# sns.histplot(
#     data=df, x=S_transformed, ax=ax, kde=True
# )
# plt.text(
#     0.75, 0.95, str,
#     transform=ax.transAxes
# )
# plt.show()





########## 기온 ##############

### Yeo-Johnson Transformation

# from sklearn.preprocessing import PowerTransformer

# tr = PowerTransformer(method='yeo-johnson')
# transformed = tr.fit_transform(df[['평균기온']]) # fit_transform의 인자는 2차원 형태의 입력만 받는다. 결과값은 2차원 numpy array
# df['transformed_기온'] = transformed.flatten()

# skewness = skew(df['transformed_기온'])
# str = f'skewness : {skewness:.2f}'

# fig, ax = plt.subplots()
# sns.histplot(
#     data=df, x='transformed_기온', ax=ax, kde=True, bins=50
# )
# plt.text(
#     0.1, 0.95, str,
#     transform = ax.transAxes
# )
# plt.show()




############ 바람 ##############

data = df['평균풍속']
boxcox_transformed_data, fitted_lambda = boxcox(data)
df['boxcox_평균풍속'] = boxcox_transformed_data

# skewness = skew(boxcox_transformed_data)
# skew_str = f'skewness = {skewness:.2f}'
# fig, ax = plt.subplots(1, 2, figsize=(12,5))
# sns.histplot(
#     data=df, x='boxcox_평균풍속', ax=ax[0], kde=True
# )
# ax[0].set_ylabel('갯수')
# ax[0].set_title('Histogram')

# plt.sca(ax[1])
# probplot(boxcox_transformed_data, dist='norm', plot=plt)
# ax[1].set_title('Q-Q Plot')
# plt.text(
#     0.05, 0.95, skew_str,
#     transform = ax[1].transAxes,
#     bbox=dict(boxstyle='square', facecolor='lightyellow')
# )

# plt.show()