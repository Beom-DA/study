# import time
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# import platform

# ################## PostgreSql DB에 csv 데이터 넣기 ####################
# '''from sqlalchemy import create_engine

# start_time = time.time()
# df_consumption_list = [
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202406_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202407_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202408_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202409_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202410_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202411_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202412_수원시.csv', encoding='euc-kr'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202501_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202502_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202503_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202504_수원시.csv'),
#     pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202505_수원시.csv'),
# ]
# new_df= pd.concat(df_consumption_list, ignore_index=True)
# engine = create_engine('postgresql+pg8000://postgres:1234@localhost:5432/Data', echo=True)

# new_df.to_sql('consumption', engine, if_exists='replace', index=False)
# end_time = time.time()

# print("걸린 시간 : {:.2f}".format(end_time - start_time))'''

# # df = pd.read_csv(r'data/날씨_데이터/수원시_바람_데이터.csv',encoding='euc-kr', skiprows=15)
# # engine = create_engine('postgresql+pg8000://postgres:1234@localhost:5432/Data', echo=True)

# # df.to_sql('wind', engine, if_exists='replace', chunksize=1000, index=False)

# #######################################################################



# ################################ 날씨 데이터에 대한 EDA 및 전처리 #################################

# df_precipitation = pd.read_csv(r'Data/날씨_데이터/수원시_강수량_데이터.csv')
# df_temperature = pd.read_csv(r'Data/날씨_데이터/수원시_기온_데이터.csv')
# df_humidity = pd.read_csv(r'Data/날씨_데이터/수원시_습도_데이터.csv')
# df_wind = pd.read_csv(r'Data/날씨_데이터/수원시_바람_데이터.csv')



# df_precipitation['날짜'] = pd.to_datetime(df_precipitation['날짜'])
# df_temperature['날짜'] = pd.to_datetime(df_temperature['날짜'])
# df_humidity['날짜'] = pd.to_datetime(df_humidity['날짜'])
# df_wind['날짜'] = pd.to_datetime(df_wind['날짜'])

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



# ###### 데이터를 그래프로 표현 ######

# # plt.show() 시 그래프의 xlabel과 ylabel에 대한 한글 폰트 깨짐을 해결하기 위한 코드
# if platform.system() == 'Windows':
#     plt.rcParams['font.family'] = 'Malgun Gothic'
# elif platform.system() == 'Darwin':
#     plt.rcParams['font.family'] = 'AppleGothic'
# else:
#     plt.rcParams['font.family'] = 'NanumGothic'

# plt.rcParams['axes.unicode_minus'] = False


# ## Scatterplot
# '''fig, ax = plt.subplots()
# sns.scatterplot(
#     data=df_weather, x='날짜', y='강수량', ax=ax
# )
# plt.show()

# fig = px.scatter(
#     data_frame=df_weather, x='날짜', y='강수량',
#     width=500, height=500
# )
# fig.show()'''


# ## Heatmap
# '''date_list = pd.date_range(start='2024-06-01', end='2025-06-01', freq='45D')
# df_weather['date_bin'] = pd.cut(df_weather['날짜'], bins=date_list)
# precipitation_list = np.arange(0, 170, 20)
# df_weather['pre_bin'] = pd.cut(df_weather['강수량'], bins=precipitation_list)

# pivot_df = df_weather.pivot_table(
#     index='date_bin', columns= 'pre_bin',
#     values='강수량', aggfunc='count'
# )'''

# # fig, ax = plt.subplots()
# # sns.heatmap(
# #     data=pivot_df, ax=ax, annot=True
# # )
# # plt.show()

# #print(pivot_df)
# '''fig = px.imshow(
#     pivot_df, x=pivot_df.columns.astype(str), y=pivot_df.index.astype(str),
#     width=850, height=500, color_continuous_scale="Blues", text_auto=True
# )
# fig.show()'''


# '''fig, ax = plt.subplots()
# sns.boxenplot(data=df_weather, y='강수량', ax= ax)
# plt.show()'''

# fig = px.box(
#     data_frame=df_weather, y='강수량',
#     width=500, height=500
# )
# fig.show()


x = 5.123123
print("이상치 : {:.2f}".format(x))