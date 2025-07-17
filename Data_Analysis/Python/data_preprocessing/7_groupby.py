import pandas as pd
import numpy as np
import seaborn as sns


# 특정 변수의 값 별로 묶어서 각종 연산 가능
# 수치형 변수의 통계 계산, 문자열 연산 등 가능
# 사용자 정의 함수 사용 가능

#df = sns.load_dataset('titanic')

'''df.groupby('sex')['survived'].mean()

df.groupby(['sex', 'class'])['survived'].mean()

df.groupby(['sex', 'class'])['survived'].agg(['mean', 'count'])'''

#변수 별 별도 통계 연산 가능
'''df = df.groupby(['sex','class'])[['survived', 'age']].agg({'survived' : 'mean', 'age' : 'max'})
print(df)'''

'''def get_IQR(data):
    _3rd = data.quantile(0.75)
    _1st = data.quantile(0.25)
    return (np.abs(_3rd - _1st) * 1.5)

df.groupby(['sex', 'class'])['age'].apply(get_IQR)'''


# 결측치 갯수 확인, 결측치를 평균값으로 대체
'''df = sns.load_dataset('penguins')
df.isna().sum()
df.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm', 'body_mass_g']].mean()
df = df.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm', 'body_mass_g']].apply(
    lambda x : x.fillna(x.mean())
)'''

####### 그룹을 임의로 나눠서 데이터 추출하기
df = pd.DataFrame(
    {
        'group' : ['A','A','A','B','B'],
        'value' : [1,1,1,10,10]
    }
)
df.groupby('group')['value'].sum()

# groupby 인자로 열 이름 이외의 다른 형태의 데이터 전달
df.groupby([0,0,1,1,1])['value'].sum()

s = pd.Series([False, False, True, True, True])
df = df.groupby(s)['value'].sum()
print(df)