import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform
from just_do_it_데이터_병합 import df


### 평균기온에 대한 이상치 탐색
# fig = px.box(
#     data_frame=df, y='평균기온',
#     width=500, height=500
# )
# fig.show()

# Q3, Q1, median = 23.55, 2.9, 14.7
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR
# count = 0
# for outlier in df['평균기온']:
#     if outlier < lower_bound or outlier > upper_bound :
#         print("이상치 : {:.2f}".format(outlier))
#         count += 1
# print("이상치 개수 : ", count) # 이상치 없음


### 강수량에 대한 이상치 탐색
# fig = px.box(
#     data_frame=df, y='강수량',
#     width=500, height=500
# )
# fig.show() # box 모양이 그래프에 나타나지 않음 --> 0값이 너무 많아서 Q3와 Q1의 값이 같기 때문에 그런 듯하다.
# #          # 그래프를 보면 강수량이 151인 데이터가 이상치처럼 보일 수 있지만 실제로 151mm는 충분히 가능한 수치기 때문에 이상치는 없는걸로 결론을 내겠다.


## 습도에 대한 이상치 탐색
# fig = px.box(
#     data_frame=df, y='평균습도',
#     width=500, height=500
# )
# fig.show()

# Q3, Q1 = 76.5, 60
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5*IQR
# upper_bound = Q3 + 1.5*IQR
# count = 0
# for outlier in df['평균습도']:
#     if outlier < lower_bound or outlier > upper_bound:
#         count += 1
#         print('이상치 : {:.2f}'.format(outlier))
# print('이상치 개수 : {}개'.format(count))



## 풍속에 대한 이상치 탐색
# fig, ax = plt.subplots()
# sns.boxenplot(
#     data=df, y='평균풍속', ax=ax
# )
# plt.show()

# fig = px.box(
#     data_frame=df, y='평균풍속', width=500, height=500
# )
# fig.show()


## 매출액에 대한 이상치 탐색
# fig = px.box(
#     data_frame=df, y='금액', width=500, height=500
# )
# fig.show()




