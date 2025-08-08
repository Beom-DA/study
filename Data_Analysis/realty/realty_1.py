################# 데이터 살펴보기 ###############

import pandas as pd

df1 = pd.read_csv(r'realty/realty_data/주택도시보증공사_전국 평균 분양가격(2019년 12월).csv', encoding = 'cp949')
df2 = pd.read_csv(r'realty/realty_data/전국 평균 분양가격(2013년 9월부터 2015년 8월까지).csv', encoding = 'cp949')

df_last = df1.copy()
df_first = df2.copy()

#print(df.head())
#print(df.tail())
#print(df_first.head())

df_last['분양가격'] = pd.to_numeric(df_last['분양가격(㎡)'], errors='coerce')
df_last['평당분양가격'] = df_last['분양가격'] * 3.3
#print(df_last.head())

df_last['전용면적'] = df_last['규모구분'].str.replace('전용면적','')
df_last['전용면적'] = df_last['전용면적'].str.replace('초과','~')
df_last['전용면적'] = df_last['전용면적'].str.replace('이하','').str.strip()

df_last = df_last.drop(columns=['규모구분','분양가격(㎡)'])
#print(df_last.info())

#print(df_last.groupby(['지역명'])['평당분양가격'].mean())
# print(df_last.groupby(['전용면적'])['평당분양가격'].mean())
#print(df_last.groupby(['지역명','전용면적'])['평당분양가격'].mean().unstack().round()) # unstack()은 groupby의 인자중 뒤에 있는 변수를 컬럼명으로 지정
# .transpose() 는 행과 열을 바꿈

pt = pd.pivot_table(data=df_last, index=['지역명'], values=['평당분양가격']) #aggfunc을 지정하지 않으면 디폴트 값은 mean값
print(pt)