
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


######################    날씨 데이터    ########################3
'''from sqlalchemy import create_engine

data = pd.read_csv(r'C:/Users/nambi/OneDrive/바탕 화면/2024_날씨데이터.csv', encoding='cp949')
df = data[['일시', '기온(°C)', '강수량(mm)', '풍속(m/s)', '습도(%)']]
df = df.rename(columns={'일시':'날짜', '기온(°C)':'기온','강수량(mm)':'강수량','풍속(m/s)':'풍속', '습도(%)':'습도'})
print(df.head())

start_time = time.time()
engine = create_engine('postgresql+pg8000://postgres:1234@localhost:5432/Data', echo=True)

df.to_sql('weather_2024', engine, if_exists='replace', index=False)
end_time = time.time()

print('소요시간 : ', end_time - start_time)'''


# w_data = pd.read_csv(r'Data/날씨_데이터/날씨데이터_2024.csv', encoding='utf-8')
# w_data['날짜'] = pd.to_datetime(w_data['날짜'])
# w_data['시간'] = w_data['날짜'].dt.hour
# w_data['날짜'] = w_data['날짜'].dt.date
# w_data['날짜'] = pd.to_datetime(w_data['날짜'])

# conditions = [
#     w_data['시간'] < 7,
#     (w_data['시간'] >= 7) & (w_data['시간'] < 9),
#     (w_data['시간'] >= 9) & (w_data['시간'] < 11),
#     (w_data['시간'] >= 11) & (w_data['시간'] < 13),
#     (w_data['시간'] >= 13) & (w_data['시간'] < 15),
#     (w_data['시간'] >= 15) & (w_data['시간'] < 17),
#     (w_data['시간'] >= 17) & (w_data['시간'] < 19),
#     (w_data['시간'] >= 19) & (w_data['시간'] < 21),
#     (w_data['시간'] >= 21) & (w_data['시간'] < 23),
#     w_data['시간'] == 23
# ]
# choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# w_data['시간'] = np.select(conditions, choices).astype(np.int64)
# #print(w_data.info())

# grouped = pd.DataFrame(w_data.groupby(['날짜', '시간'])[['기온', '강수량','풍속','습도']].agg('mean').reset_index())
# df_weather = grouped.copy()
# #print(grouped.info())



# ######################## 소비 데이터 ##############################
# df_init = pd.DataFrame()

# for i in range(1, 13):
#     if i < 10 :
#         index = '0'+ str(i)
#     else : index = str(i)

#     if index == '12':
#         data = pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_2024' + index + '_수원시.csv', encoding='cp949')
#     else:
#         data = pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_2024' + index + '_수원시.csv', encoding='utf-8')
#     data_1 = data[['ta_ymd', 'card_tpbuz_nm_2', 'hour', 'sex', 'day', 'cnt']]
#     df_1 = data_1.rename(columns={'ta_ymd':'날짜', 'hour':'시간', 'sex':'성별', 'day':'요일', 'card_tpbuz_nm_2' : '물품분류'})
    
#     df_1['날짜'] = pd.to_datetime(df_1['날짜'], format='%Y%m%d')
#     df_1['날짜'] = df_1['날짜'].dt.strftime('%Y-%m-%d')
#     df_1['날짜'] = pd.to_datetime(df_1['날짜'], format='%Y-%m-%d')



#     df_init = pd.concat([df_init, df_1], axis=0)

# df_comsumption = df_init.copy()
# #print(df_comsumption.info())


# df_merge = pd.merge(df_comsumption, df_weather, on=['날짜', '시간'], how='inner').reset_index()
# index_series = df_merge['index']
# df_merge = df_merge.drop('index', axis=1)
# df_merge['월'] = df_merge['날짜'].dt.month
# df_merge = df_merge.reindex(columns=['날짜','월','요일','시간','성별','기온','강수량','풍속','습도','cnt'])
# print(df_merge.head(40))



data = pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_202401_수원시.csv', encoding='utf-8')
data_1 = data[['ta_ymd', 'card_tpbuz_nm_2', 'hour', 'sex', 'day', 'cnt']]
df_1 = data_1.rename(columns={'ta_ymd':'날짜', 'hour':'시간', 'sex':'성별', 'day':'요일', 'card_tpbuz_nm_2' : '물품분류'})
df_1['물품분류'] = df_1['물품분류'].astype('category')
df_1['encoded_물품분류'] = df_1['물품분류'].cat.codes

mapping = dict(enumerate(df_1['물품분류'].cat.categories))
print(df_1.head(30))
#print(mapping)





