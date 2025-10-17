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
from just_do_it_정규성_변환 import df


############### 금액 ###################

# ## Z-Score Scaling
# from sklearn.preprocessing import StandardScaler
 
# scaler = StandardScaler()  
# scaled_data = scaler.fit_transform(df['log_금액'].values.reshape(-1,1)) # standardscaler는 2차원 배열 입력을 기대하는데 Series는 1차원이라서 에러가 난다.
# scaled_series = pd.Series(scaled_data.flatten(), index=df['log_금액'].index)
# print('Z-score Scaling mean_value : {:.2f}'.format(scaled_series.mean()))
# print('Z-score Scaling std_value : {:.2f}'.format(scaled_series.std()))



# ## Robust Scaling
from sklearn.preprocessing import RobustScaler

r_scaler = RobustScaler()
r_scaled_data = r_scaler.fit_transform(df['log_금액'].values.reshape(-1,1))
r_scaled_series_money = pd.Series(r_scaled_data.flatten(), index=df['log_금액'].index)
df['r_scaled_금액'] = r_scaled_series_money
# print('Robust Scaling median_value : {:.2f}'.format(r_scaled_series.median()))

# fig, ax = plt.subplots(1,2)
# sns.boxenplot(
#     data=df, y='log_금액', ax=ax[0]
# )
# sns.boxenplot(
#     data=df, y='r_scaled_금액', ax=ax[1]
# )
# ax[0].set_title('log transformation')
# ax[1].set_title('Robust Scaling Graph')
# plt.show()





# ################ 기온 ###################

# ## Robust Scaling
# from sklearn.preprocessing import RobustScaler

data_temp = df['기온']
r_scaler = RobustScaler()
r_scaled_data_temp = r_scaler.fit_transform(data_temp.values.reshape(-1,1))
r_scaled_series_temp = pd.Series(r_scaled_data_temp.flatten())
df['r_scaled_기온'] = r_scaled_series_temp
# print('중앙값 : ', r_scaled_series.median())

# Q3 = r_scaled_series.quantile(0.75)
# Q1 = r_scaled_series.quantile(0.25)

# IQR = Q3-Q1

# print('IQR : ', IQR)





################# 강수량 ########################

### Robust Scaling
# from sklearn.preprocessing import RobustScaler

data_rain = df['강수량']
r_scaler = RobustScaler()
r_scaled_data_rain = r_scaler.fit_transform(data_rain.values.reshape(-1,1))
r_scaled_series_rain = pd.Series(r_scaled_data_rain.flatten())
df['r_scaled_강수량'] = r_scaled_series_rain

# print('중앙값 : {:.2f}'.format(r_scaled_series.median()))




################ 습도 ################

### Z-score Scaling
from sklearn.preprocessing import StandardScaler

data_humidity = df['습도']
scaler = StandardScaler()
scaled_data_humidity = scaler.fit_transform(data_humidity.values.reshape(-1,1))
scaled_series_humidity = pd.Series(scaled_data_humidity.flatten())
df['scaled_습도'] = scaled_series_humidity

# print('중앙값 : ', scaled_series.median())







############## 바람 ################
#from sklearn.preprocessing import StandardScaler

data_wind = df['boxcox_풍속']
scaler = StandardScaler()
scaled_data_wind = scaler.fit_transform(data_wind.values.reshape(-1,1))
scaled_series_wind = pd.Series(scaled_data_wind.flatten())
df['scaled_풍속'] = scaled_series_wind

#print('중앙값 : ', scaled_series_wind.median())


# NaN값 찾기
#print(df.isna().sum()[df.isna().sum() > 0])

# print(df[df['r_scaled_기온'].isna()])
# print(df[df['r_scaled_강수량'].isna()])

df = df.dropna()
#print(df.isna().sum()[df.isna().sum() > 0])
#print(df.info())


df_1 = df.drop(['날짜', '기온','강수량','풍속','습도', 'log_금액', 'boxcox_풍속', '금액', '물품분류'], axis=1)
#print(df_1.info)
#--> df_1은 11개 컬럼

#### 샘플링
# from sklearn.model_selection import train_test_split
# df_sample, _ = train_test_split(df, stratify=df['물품분류','시간','성별','나이','요일'].astype(str), train_size=500000, random_state=42)
df_sample = df_1.sample(n=500000, random_state=42)


#### 원-핫 인코딩
category_col = ['시간', '성별', '나이', '요일']
df_encoded = pd.get_dummies(df_sample, columns=category_col, drop_first=True)
df = df_encoded

#print(df.info())