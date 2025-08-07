import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform

################## PostgreSql DB에 csv 데이터 넣기 ####################
'''from sqlalchemy import create_engine

start_time = time.time()
df_consumption_list = [
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202406_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202407_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202408_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202409_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202410_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202411_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202412_수원시.csv', encoding='euc-kr'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202501_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202502_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202503_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202504_수원시.csv'),
    pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202505_수원시.csv'),
]
new_df= pd.concat(df_consumption_list, ignore_index=True)
engine = create_engine('postgresql+pg8000://postgres:1234@localhost:5432/Data', echo=True)

new_df.to_sql('consumption', engine, if_exists='replace', index=False)
end_time = time.time()

print("걸린 시간 : {:.2f}".format(end_time - start_time))'''

# df = pd.read_csv(r'data/날씨_데이터/수원시_바람_데이터.csv',encoding='euc-kr', skiprows=15)
# engine = create_engine('postgresql+pg8000://postgres:1234@localhost:5432/Data', echo=True)

# df.to_sql('wind', engine, if_exists='replace', chunksize=1000, index=False)

#######################################################################



################################ 날씨 데이터 병합 #################################

# df_precipitation = pd.read_csv(r'Data/날씨_데이터/수원시_강수량_데이터.csv')
# df_temperature = pd.read_csv(r'Data/날씨_데이터/수원시_기온_데이터.csv')
# df_humidity = pd.read_csv(r'Data/날씨_데이터/수원시_습도_데이터.csv')
# df_wind = pd.read_csv(r'Data/날씨_데이터/수원시_바람_데이터.csv')



# df_precipitation['날짜'] = pd.to_datetime(df_precipitation['날짜'], format='%Y-%m-%d')
# df_temperature['날짜'] = df_temperature['날짜'].str.strip()
# df_temperature['날짜'] = pd.to_datetime(df_temperature['날짜'], format='%Y-%m-%d')
# df_humidity['날짜'] = pd.to_datetime(df_humidity['날짜'], format='%Y-%m-%d')
# df_wind['날짜'] = pd.to_datetime(df_wind['날짜'], format='%Y-%m-%d')

# ## 날씨 데이터의 날짜에 대한 범주를 2024-06-01 ~ 2025-05-30으로 맞춘다.
# df_precipitation = df_precipitation.query('날짜 >= "2024-06-01" & 날짜 <= "2025-05-30"')
# df_temperature = df_temperature.query('날짜 >= "2024-06-01" & 날짜 <= "2025-05-30"')
# df_humidity = df_humidity.query('날짜 >= "2024-06-01" & 날짜 <= "2025-05-30"')
# df_wind = df_wind.query('날짜 >= "2024-06-01" & 날짜 <= "2025-05-30"')


# ## 강수량, 기온, 습도, 바람에 대한 데이터들을 df_weather라는 하나의 데이터프레임에 merge한다.
# df_list = [df_precipitation, df_temperature, df_humidity, df_wind]
# df_weather = df_precipitation

# for i in range(len(df_list)-1):
#     df_weather = pd.merge(df_weather,df_list[i+1], on='날짜', how='left')



# ## 결측치를 0으로 대체한다.
# df_weather['강수량'] = df_weather['강수량'].fillna(0)
# '''print(df_weather.info())'''

# ######################### 날씨 데이터와 소비 데이터 병합 ######################
# df_consumption = pd.read_csv(r'data/소비_데이터/수원시_소비_데이터.csv')
# df_consumption['날짜'] = df_consumption['날짜'].astype(int).astype(str).str.strip() ## .str을 쓰는 이유 : df_consumption['날짜']는 series기 때문에 .strip()만 사용하면 에러가 발생한다.
# df_consumption['날짜'] = (                                                         ## .str을 사용하면 '각 행의 문자열마다' 라는 의미가 추가된다.
#     df_consumption['날짜'].str[:4] + '-' +  # 연
#     df_consumption['날짜'].str[4:6] + '-' +  # 월
#     df_consumption['날짜'].str[6:]           # 일
# )
# df_consumption['날짜'] = pd.to_datetime(df_consumption['날짜'], format='%Y-%m-%d')
# df_consumption = df_consumption.query('날짜 >= "2024-06-01" & 날짜 <= "2025-05-30"')
# df = pd.merge(df_consumption, df_weather, on='날짜', how='left')

df = pd.read_csv(r'Data/통합데이터.csv')
df['날짜'] = pd.to_datetime(df['날짜'], format='%Y-%m-%d')
df['강수량'] = df['강수량'].fillna(0)
#print(df['강수량'].info())


### 원-핫 인코딩
category_col = ['물품분류', '시간', '성별', '나이', '요일']
df_encoded = pd.get_dummies(df, columns=category_col, drop_first=True)
df = df_encoded

# 금액이 0인 데이터에 대해 삭제
df = df[df['금액'] > 0]
#print((df['금액']<=0).sum())

#print(df['성별_M'].value_counts())



