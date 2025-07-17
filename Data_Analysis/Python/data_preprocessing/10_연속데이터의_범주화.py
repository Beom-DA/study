####### 연속 데이터를 그룹화하여 범주형 데이터로 분석하기

### 수치형 변수의 범주화
# pandas cut함수를 이용하여 특정 수치 구간 별로 데이터를 범주화
# 범주화된 구간을 x축으로 하는 boxplot()이나 groupby메소드를 통해 통계적 인사이트를 얻을 수 있음
# 예시) 나이 43세 --> 30세 이상 40세 미만

import pandas as pd
import numpy as np

df = pd.read_csv(r'data_analysis_adv/datasets/German_credit/German_credit.csv')
#print(df.head())

#print(pd.cut(df['Age'], bins = 8).reset_index().groupby('Age').size())

# bins 인자에 범주화할 구간 개수 혹은 구간을 list나 array 형태로 전달 가능
'''bins = [10,20,30,40,50,60,70,80]
print(pd.cut(df['Age'], bins = bins))
'''
# cut 함수 : 동일한 길이의(혹은 사용자 정의)구간으로 데이터를 나눌 때
# qcut 함수 : n개의 구간에 포함되는 데이터의 개수를 동일하게 나누고자 할 때
# 중복된 데이터가 많을 경우, 구간에 포함되는 데이터의 개수가 동일하지 않을 수 있음

#print(pd.qcut(df['Age'], q = 8))
print(pd.qcut(df['Age'], q = 8).reset_index().groupby('Age').size())