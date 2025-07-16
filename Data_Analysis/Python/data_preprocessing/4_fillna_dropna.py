import pandas as pd
import numpy as np

df = pd.read_csv(r'datasets/bookings/bookings.csv')

####### isna 메소드
# 값이 결측치인 경우 True를, 아닌 경우 False를 반환
# sum 메소드와 함께 사용하여 결측치의 개수 확인 가능
'''index = df[df['Rating'].isna()].head(5).index'''
#print(index)

####### fillna 메소드
# 결측치를 인자에 전달하는 값으로 대체
# method 인자에 'ffill'(front fill) 전달 시 앞의 값으로 뒤의 결측치 대체
# method 인자에 'bfill'(back fill) 전달 시 뒤의 값으로 앞의 결측치 대체
'''df['Rating'] = df['Rating'].fillna(df['Rating'].mean())'''
#print(df.loc[:, 'Rating'])

'''s = pd.Series([1, np.nan, np.nan, 2, np.nan, 3])
s = s.fillna(method='ffill')
s = s.fillna(method='bfill')
print(s)'''



####### dropna 메소드
# 결측치가 포함된 특정 행/열을 삭제
# axis 인자 : 0은 행, 1은 열을 뜻함
# subset 인자 : 결측치를 제거할 레이블 특정
# how 인자 : 'all' 전달 시 모든 값이 결측치인 경우에만 삭제
'''df = df.dropna()
df = df.dropna(axis = 1)'''
'''df = df.dropna(subset='Review', axis = 0)
df['Review'].isna().sum() --> False는 0가 동일한 값이기 때문에 sum()을 하면 0이 나온다.'''

