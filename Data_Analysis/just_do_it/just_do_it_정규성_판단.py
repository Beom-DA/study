from just_do_it_데이터_병합 import df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform
from scipy.stats import skew
from scipy.stats import probplot


if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'

plt.rcParams['axes.unicode_minus'] = False


############ 기온 데이터 ##############

## 히스토 그램  + skewness + Q-Q plot

# data = df['평균기온']
# skewness = skew(data)
# skew_str = f'skewness : {skewness:.2f}'

# fig, ax = plt.subplots(1, 2, figsize=(12,5))
# sns.histplot(
#     data=df, x='평균기온', ax=ax[0], bins=50, kde=True
# )
# plt.sca(ax[1])
# probplot(data, dist='norm', plot=plt)
# plt.text(
#     0.1, 0.95, skew_str,
#     transform = ax[1].transAxes
# )
# ax[0].set_title('Histogram')
# plt.show() #--> 정규성 변환 필요 (Yeo-Johnson 변환을 쓰면 될 것 같다.)









