import pandas as pd
import numpy as np

####### 데이터를 처음 만나면 하는 것들

### head & info 메소드
# 데이터의 샘플을 직접 눈으로 확인(상위 n개 행)
# 데이터의 크기(길이), 열, 결측치 등 확인

df = pd.read_csv(r'data_analysis_adv/datasets/Uber/Uber.csv')
#print(df.info())


### 변수별 확인
# 변수별 의미하는 바에 맞게 데이터 타입 변경
# 변수 내 데이터 특이점 확인(이상치, 결측값, 분포 등)

df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors = 'coerce')
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], errors = 'coerce')
df = df.sort_values(['START_DATE*', 'END_DATE*'])
# print(df['START_DATE*'].unique())  START_DATE*열에 결측치(NaT)이 존재함을 확인

### value_counts 메소드
# 범주형 변수에 활용
# 변수의 고유값과 고유값 별 빈도수 확인

#df = df['CATEGORY*'].value_counts()
#df = df['START*'].value_counts()
#df['STOP*'].value_counts()
#print(df)

'''df['PURPOSE*'].value_counts()
df['PURPOSE*'].isna().sum()'''

### describe 메소드
# 주로 수치형 변수에 활용
# 변수의 평균, 분위수, 최대/최소 등 대표 통계값 확인
# 평균 대 표준편차 비 등으로 변수의 분포 및 이상치 여부 확인 가능

df['MILES*'].describe()
df[df['MILES*'] == df['MILES*'].max()]
df = df.drop(1155)
#print(df['MILES*'].describe())


### 파생 변수 추가
# 데이터 분석의 목적에 따라 주어진 변수들로 새로운 변수를 생성
# 머신러닝 분야에서 보델의 성능을 높이는데 사용 가능

df['DURATION*'] = (df['END_DATE*'] - df['START_DATE*']).dt.total_seconds() / 60
#print(df['DURATION*'])


### groupby 메소드
# 특정 변수(들)의 데이터 그룹별 변수의 통계값 확인

#df = df.groupby(['CATEGORY*','PURPOSE*'])[['MILES*','DURATION*']].agg(['mean','std','count'])
#print(df)


### 변수 간 상관관계 파악
# 데이터를 구성하는 변수 간 상관관계 파악
# corr() 메소드를 이용하거나, 시각화를 통한 방법 등이 있음

#df = df[['MILES*', 'DURATION*']].corr()

import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

df = df.dropna()
s, i, r, _, _ = linregress(df['MILES*'], df['DURATION*'])
# s는 기울기, i는 y절편, r은 스피어만 상관계수, _(언더바)는 변수를 받아오고 받아온 즉시 버리겠다.
fig, ax = plt.subplots() #fig는 도화지, ax는 컷
sns.regplot(
    x = 'MILES*', y = 'DURATION*', data = df, ax = ax,
    line_kws={
        'label' : 'y={:.2f}x + {:.2f}, R^2={:.2f}'.format(s, i, r**2)
    }
)
plt.legend()
plt.show()