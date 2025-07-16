import pandas as pd
import numpy as np

####### quantile 메소드
# 수치형 데이터의 분위수 반환
# 0부터 1사이의 분위수 값을 인자로 전달
# interpolation 인자에 linear, lower, higher, nearest, midpoint 전달가능(기본 값은 linear)
df = pd.read_csv(r'datasets/bookings/bookings.csv')
df['Total_Review'] = df['Total_Review'].map(lambda x : str(x).replace('external','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x : str(x).replace('review','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x : str(x).replace(',','').strip())
df['Total_Review'] = df['Total_Review'].astype('float')

quantile = [0, 0.2, 0.4, 0.6, 0.8, 1]
for idx in quantile:
    q = df['Total_Review'].quantile(idx, interpolation = 'midpoint')
    print(f'quantile({idx}) is {q}')