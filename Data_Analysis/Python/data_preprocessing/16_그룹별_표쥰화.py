####### 데이터 내 그룹별 표준화

### 데이터 표준화
# 최대 최소 표준화, 평균 표준화 등
# 특정 변수의 데이터 그룹별로 표준화를 수행해야 하는 경우

import pandas as pd
import numpy as np

df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])
df.groupby('inspection_step')['value'].mean()

# inspection_step 변수의 값 별로 표준화 진행
df['normalized1'] = df.groupby('inspection_step')['value'].transform(lambda x : (x - x.mean()) / x.std())
#print(df['normalized1'])

# inspection_step 변수의 가장 첫 번째 값으로 표준화 진행
temp = df.sort_values(['inspection_step', 'date']).drop_duplicates('inspection_step')
#print(temp)
temp = temp.set_index('inspection_step')['value'] # set_index
df = df.set_index('inspection_step')              # set_index  index를 바꾸는 이유는 
df['normalized2'] = df['value'] - temp            # 이 코드처럼 두개의 열을 서로 빼기 위해서
df = df.reset_index()
print(df['normalized2'])