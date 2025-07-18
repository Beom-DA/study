####### 정렬된 인덱스에서의 행 슬라이싱

### 행 슬라이싱
# 시계열 데이터의 날짜/시간 슬라이싱
# 정렬된 문자열 인덱스일 경우 사전식 검색 가능

import pandas as pd
import numpy as np

df = pd.read_csv(r'data_analysis_adv/datasets/Covid19-US/us_confirmed.csv')
df['Date'] = pd.to_datetime(df['Date'])

df = df.set_index('Date').sort_values('Date')
# 년월일까지 지정하지 않아도 슬라이싱 가능
#print(df['2020-01' : '2020-02'])

df = df.reset_index().set_index('Province/State').sort_index()
#print(df.index.unique())
# 사전식 슬라이싱 가능
print(df['Ca': 'Df'])