####### Datetime Resample과 Groupby 동시에 수행하기

### 날짜/시간 형식을 포함한 두 개 이상의 변수를 기준으로 groupby하기
# 날짜/시간 변수를 특정 그룹으로 resample하고, 동시에 추가 변수 그룹과 groupby
# 날짜/시간 변수를 인덱스로 설정 후 pandas Grouper 이용

import pandas as pd
import numpy as np

df = pd.read_csv(r'data_analysis_adv/datasets/Covid19-US/us_confirmed.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date').sort_index()
#print(df['Province/State'].nunique()) --> nunique()는 고유값의 갯수

# Province/State 변수가 너무 많아 상위 3개만 필터링
states = df['Province/State'].unique()[0:3]
df= df[df['Province/State'].isin(states)]
#print(df)

df = df.groupby([pd.Grouper(freq='1M'), 'Province/State'])['Case'].mean()
print(df['2020-01' : '2020-06'])