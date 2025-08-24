import platform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import missingno as msno
from scipy import stats

if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'

plt.rcParams['axes.unicode_minus'] = False


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


w_data = pd.read_csv(r'Data/날씨_데이터/날씨데이터_2024.csv', encoding='utf-8')
w_data['날짜'] = pd.to_datetime(w_data['날짜'])
w_data['시간'] = w_data['날짜'].dt.hour
w_data['날짜'] = w_data['날짜'].dt.date
w_data['날짜'] = pd.to_datetime(w_data['날짜'])

conditions = [
    w_data['시간'] < 7,
    (w_data['시간'] >= 7) & (w_data['시간'] < 9),
    (w_data['시간'] >= 9) & (w_data['시간'] < 11),
    (w_data['시간'] >= 11) & (w_data['시간'] < 13),
    (w_data['시간'] >= 13) & (w_data['시간'] < 15),
    (w_data['시간'] >= 15) & (w_data['시간'] < 17),
    (w_data['시간'] >= 17) & (w_data['시간'] < 19),
    (w_data['시간'] >= 19) & (w_data['시간'] < 21),
    (w_data['시간'] >= 21) & (w_data['시간'] < 23),
    w_data['시간'] == 23
]
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
w_data['시간'] = np.select(conditions, choices).astype(np.int64)
#print(w_data.info())

grouped = pd.DataFrame(w_data.groupby(['날짜', '시간'])[['기온', '강수량','풍속','습도']].agg('mean').reset_index())
df_weather = grouped.copy()
#print(grouped.info())



######################## 소비 데이터 ##############################
df_init = pd.DataFrame()

for i in range(1, 13):
    if i < 10 :
        index = '0'+ str(i)
    else : index = str(i)

    if index == '12':
        data = pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_2024' + index + '_수원시.csv', encoding='cp949')
    else:
        data = pd.read_csv(r'data/소비_데이터/tbsh_gyeonggi_day_2024' + index + '_수원시.csv', encoding='utf-8')
    data_1 = data[['ta_ymd', 'card_tpbuz_nm_2', 'hour', 'sex', 'day', 'cnt']]
    df_1 = data_1.rename(columns={'ta_ymd':'날짜', 'hour':'시간', 'sex':'성별', 'day':'요일', 'card_tpbuz_nm_2' : '물품분류'})
    
    df_1['날짜'] = pd.to_datetime(df_1['날짜'], format='%Y%m%d')
    df_1['날짜'] = df_1['날짜'].dt.strftime('%Y-%m-%d')
    df_1['날짜'] = pd.to_datetime(df_1['날짜'], format='%Y-%m-%d')

    conditions = [
        '2024-01-01','2024-02-09','2024-02-10','2024-02-11','2024-02-12','2024-03-01','2024-04-10','2024-05-05','2024-05-06','2024-05-15',
        '2024-06-06','2024-08-15','2024-09-16','2024-09-17','2024-09-18','2024-10-03','2024-10-09','2024-12-25'
    ]
    df_1['공휴일'] = df_1['날짜'].isin(conditions).astype(int)
    
    df_1['성별'] = df_1['성별'].apply(lambda x : 1 if x == 'M' else 0) # 여자면 0 남자면 1

    df_init = pd.concat([df_init, df_1], axis=0)

df_init['물품분류'] = df_init['물품분류'].astype('category')
df_init['encoded_물품분류'] = df_init['물품분류'].cat.codes
mapping = dict(enumerate(df_init['물품분류'].cat.categories)) # label encoding 한 데이터 저장
df_init = df_init.drop(columns='물품분류')
df_init = df_init.rename(columns={'encoded_물품분류':'분류'})
df_comsumption = df_init.copy()
#print(df_comsumption.info())


df_merge = pd.merge(df_comsumption, df_weather, on=['날짜', '시간'], how='inner').reset_index()
index_series = df_merge['index']
df_merge = df_merge.drop('index', axis=1)
df_merge['월'] = df_merge['날짜'].dt.month
df_merge = df_merge.reindex(columns=['날짜','월','요일', '공휴일','시간', '분류', '성별','기온','강수량','풍속','습도','cnt'])

category_list = ['월','요일', '공휴일', '시간','분류','성별']
df_merge[category_list] = df_merge[category_list].astype('category')
#print(df_merge.info())


'''0: '가례서비스', 1: '가전제품', 2: '간이주점', 3: '건강/기호식품', 4: '경기관람', 5: '고기요리', 6: '공공기관', 7: '공연관람', 8: '광고/인쇄/인화', 9: '교통서비스', 
10: '금융상품/서비스', 11: '기술/직업교육학원', 12: '기업', 13: '기타결제', 14: '기타교육', 15: '기타용품', 16: '기타의료', 17: '단체', 18: '닭/오리요리', 19: '독서실/고시원', 
20: '렌탈서비스', 21: '무 점포서비스', 22: '문화서비스', 23: '미용서비스', 24: '방문판매', 25: '방송/미디어', 26: '별식/퓨전요리', 27: '보안/운송', 28: '부동산', 29: '부페',
30: '분식', 31: '사무/교육용품', 32: '사우나/휴게시설', 33: '서적/도서', 34: '선물/완구', 35: '세탁/가사서비스', 36: '수리서비스', 37: '수의업', 38: '숙박', 
39: '스포츠/레져용품', 40: '시스템/통신', 41: '악기/공예', 42: '양식', 43: '여행/유학대행', 44: '연료판매', 45: '예체능계학원', 46: '외국어학원', 47: '요가/단전/마사지', 
48: '유아교육', 49: '유아용품', 50: '유흥주점', 51: '음/식료품소매', 52: '음 식배달서비스', 53: '의복/의류', 54: '의약/의료품', 55: '인터넷쇼핑', 56: '인테리어/가정용품', 
57: '일반병원', 58: '일반스포츠', 59: '일식/수산물', 60: '입시학원', 61: '자동차학원', 62: '전문서비스', 63: '전시장', 64: '제과/제빵/떡/케익', 65: '제조/도매', 66: '종교',
67: '종합병원', 68: '종합소매점', 69: '중식', 70: '차량관리/부품', 71: '차량관리/서비스', 72: '차량판매', 73: '취미/오락', 74: '커피/음료', 75: '특화병원', 76: '패션잡화', 
77: '패스트푸드', 78: '학교', 79: '한식', 80: '화장품소매', 81: '회비/공과금', 82: '휴게소/대형업체'
'''


# grouped = pd.DataFrame(df_merge.groupby('날짜')['cnt'].agg('sum').reset_index()).plot(x='날짜', y='cnt', kind='line')
# plt.show()

# grouped = df_merge.groupby('날짜')['cnt'].agg('sum')
# min_date = grouped.idxmin()
#print(min_date) --> 2024-02-10은 구정이었기 때문에 카드 매출 건수가 급격히 줄어들었다. 마찬가지로 추석에도 이럴것이다.(9월 17일)
# 구정과 추석을 제외한 나머지 날짜에 대해서는 대체적으로 매출건수가 비슷함.


# grouped_df = grouped.reset_index()
# print(grouped.describe())


#print(df_merge.info())
# msno.matrix(df_merge, figsize=(12,5))
# plt.show()


# print(df_merge['강수량'].describe())




# grouped = df_merge.groupby(['날짜','시간'])[['기온','강수량','풍속','습도']].agg('mean').reset_index()
# fig, ax = plt.subplots(2,2, figsize=(12,5))

# sns.histplot(data=grouped, x='기온', ax = ax[0][0])
# sns.histplot(data=grouped, x='강수량', ax = ax[0][1])
# sns.histplot(data=grouped, x='풍속', ax = ax[1][0])
# sns.histplot(data=grouped, x='습도', ax = ax[1][1])
# ax[0][0].set_title('기온')
# ax[0][1].set_title('강수량')
# ax[1][0].set_title('풍속')
# ax[1][1].set_title('습도')
# plt.tight_layout()
# plt.show()



df_merge = df_merge.drop(columns='강수량')
# print(df_merge.info())

df_merge['습도'] = df_merge['습도'].ffill()
# msno.matrix(df_merge, figsize=(12,5))
# plt.show()

# fig, ax = plt.subplots(2,3, figsize=(12,8))
# sns.boxplot(data=df_merge, y='기온', ax=ax[0][0])
# sns.boxplot(data=df_merge, y='풍속', ax=ax[0][1])
# sns.boxplot(data=df_merge, y='습도', ax=ax[0][2])

# sns.boxplot(data=df_merge, x='월', y='기온', ax=ax[1][0])
# sns.boxplot(data=df_merge, x='월', y='풍속', ax=ax[1][1])
# sns.boxplot(data=df_merge, x='월', y='습도', ax=ax[1][2])


# plt.tight_layout()
# plt.show()



#fig, ax = plt.subplots()

#sns.boxplot(data=df_merge, y='cnt', ax=ax[0])
#plt.show()

# print(df_merge.shape)
# print(df_merge['cnt'].describe())

# print((df_merge['cnt'] == 0).sum())

df_merge_without_outliers = df_merge[np.abs(df_merge['cnt'] - df_merge['cnt'].mean()) <= (3*df_merge['cnt'].std())] # 이상치를 제거한 종속변수
df_merge_without_outliers = df_merge_without_outliers[df_merge_without_outliers['cnt']>0]
# print(df_merge_without_outliers.shape)
# print(df_merge_without_outliers['cnt'].describe())



#print(df_merge.columns)
# df_corr = df_merge_without_outliers[['월', '요일', '공휴일', '시간', '분류', '성별', '기온', '풍속', '습도', 'cnt']].corr()
# corr = np.array(df_corr)
# corr[np.tril_indices_from(corr)] = False
# fig, ax = plt.subplots()
# sns.heatmap(data=df_corr, mask=corr, annot=True)
# plt.show()




#fig, ax = plt.subplots(1,2)
# sns.histplot(data=df_merge_without_outliers, x='cnt', ax=ax[0], kde=True) 
# stats.probplot(df_merge_without_outliers['cnt'], dist='norm', fit=True, plot=ax[1]) # fit=True -> 회귀선을 그린다.
# sns.histplot(np.log1p(df_merge_without_outliers['cnt']), ax=ax[0], kde=True) 
# stats.probplot(np.log1p(df_merge_without_outliers['cnt']), dist='norm', fit=True, plot=ax[1])
# plt.show()



# boxcox_y, lambda_ = stats.boxcox(df_merge_without_outliers['cnt'])
# fig, ax = plt.subplots(1,2)
# sns.histplot(boxcox_y, ax=ax[0], kde=True) 
# stats.probplot(boxcox_y, dist='norm', fit=True, plot=ax[1])
# plt.show()


# grouped = df_merge_without_outliers.groupby('요일')['cnt'].agg('sum').reset_index()
# sns.lineplot(data=grouped, x='요일', y='cnt', estimator=sum)
# plt.show()
# grouped = df_merge_without_outliers.groupby('공휴일')['cnt'].agg('mean').reset_index()
# sns.barplot(data=grouped, x='공휴일', y='cnt')
# plt.show()
# grouped = df_merge_without_outliers.groupby('성별')['cnt'].agg('sum').reset_index()
# sns.barplot(data=grouped, x='성별', y='cnt')
# plt.show()
# grouped = df_merge_without_outliers.groupby(['날짜','기온'])['cnt'].agg('sum').reset_index()
# sns.scatterplot(data=grouped, x='기온', y='cnt')
# plt.show()
# grouped = df_merge_without_outliers.groupby('월')['cnt'].agg('sum').reset_index()
# sns.barplot(data=grouped, x='월', y='cnt')
# plt.show()
# grouped = df_merge_without_outliers.groupby('시간')['cnt'].agg('sum').reset_index()
# sns.barplot(data=grouped, x='시간', y='cnt')
# plt.show()
#grouped = df_merge_without_outliers.groupby('분류')['cnt'].agg('sum').reset_index()
# sns.barplot(data=grouped, x='분류', y='cnt')
# plt.xticks(rotation=30)
# plt.show()








############### 계층적 샘플링 ##################
from sklearn.model_selection import train_test_split

df_merge_without_outliers['stratify'] = df_merge_without_outliers['요일'].astype(str) + '_' + df_merge_without_outliers['시간'].astype(str) + '_' +df_merge_without_outliers['분류'].astype(str)
counts = df_merge_without_outliers['stratify'].value_counts()
df_stratify_filtered = df_merge_without_outliers[df_merge_without_outliers['stratify'].isin(counts[counts >= 2].index)]
sample_df , _ = train_test_split(df_stratify_filtered, train_size=0.1, stratify=df_stratify_filtered['stratify'], random_state=42)

print(sample_df.info())
print(sample_df.shape)









# from sklearn.ensemble import RandomForestRegressor
# rfmodel = RandomForestRegressor(n_estimators=100)
# train_x = 
# model_fit = rfmodel.fit(sample_df)