import pandas as pd
import numpy as np

####### info 메소드
# dataframe의 정보 확인
# 데이터 쿼리 후 가장 먼저 사용하여 데이터 탐색을 위한 유익한 정보 확인 가능

####### describe 메소드
# 수치형 변수들에 대한 요약 통계량 확인
# 데이터의 개수, 평균, 표준편차, 최대/최소, 사분위수
# include 인자에 "object" 전달 시, 범주형 변수에 대한 고유값, 최빈값 확인 가능
'''df.describe()
df.describe(include = 'object')'''


####### value_counts 메소드
df = pd.read_csv(r'datasets/bookings/bookings.csv')
#print(df['Review'].value_counts())
'''df.loc[df['Review'] == 'Superb 9.0', 'Review'] = 'Superb '
df.loc[df['Review'] == 'Exceptional 10', 'Review'] = 'Exceptional '
print(df['Review'].value_counts())'''

####### unique 메소드
# 특정 변수의 모든 고유값 반환
#print(df['Total_Review'].unique())
df['Total_Review'] = df['Total_Review'].map(lambda x : str(x).replace('external','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x : str(x).replace('review','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x : str(x).replace(',','').strip())
df['Total_Review'] = df['Total_Review'].astype('float')
print(df['Total_Review'].describe())
