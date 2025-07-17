####### 이상치를 다루는 방법

### 이상치를 다룰 때 사용할 수 있는 메소드
# 우선 describe()와 시각화를 통해 데이터 내 이상치 유무 판단
# clip : 인자로 전달된 최대/최소 값보다 크거나 작은 것들을 최대/최소로 치환
# quantile : 변수의 분위수를 구함

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'data_analysis_adv/datasets/weight_height/weight_height.csv')
#print(df.describe())
sns.scatterplot(x='Weight', y='Height', data=df)
#plt.show()

# 이상치 제거 방법 1
'''df_new = df.query('Weight < 350')'''
# 이상치 제거 방법 2
criteria = df['Weight'].quantile(0.9999) # 여기서 quantile안의 파라미터는 분석가의 판단에 따라 값이 다를 수 있다.
df_new = df[df['Weight'] < criteria]
sns.scatterplot(x = 'Weight', y = 'Height', data = df_new)

#이상치 치환 방법(clip 이용)
df[df['Weight'] > 390].index #--> 인덱스 값 : 2014
df['Weight'] = df['Weight'].clip(50,300) #--> 최대 최소를 각각 300,50으로 치환
print(df.iloc[2014]) #--> 치환 후 이상치 인덱스 확인



