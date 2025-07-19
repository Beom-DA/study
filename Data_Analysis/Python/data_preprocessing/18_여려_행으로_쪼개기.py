####### 하나의 행을 여러 개의 행으로 쪼개기

### explode 메소드
# dataframe의 특정 변수가 list형식으로 이루어졌을때, explode 메소드를 통해 행 나누기 가능

# product 데이터셋의 세 개의 path 행을 하나로 합치는 작업 그대로 반복
import pandas as pd
import numpy as np

df = pd.read_csv(r'data_analysis_adv/datasets/product/product.csv')
df['path'] = df.groupby('product_id')['operator'].transform(lambda x : '_'.join(x))
df['path'] = df['factory'] + '_' + df['path']
df = df.drop_duplicates('product_id')
df = df[['date', 'product_id', 'passfail', 'path']]
#print(df['path'].head())

# 위의 과정을 이제 반대로 시행
df['factory'] = df['path'].map(lambda x : x[0:2])
df['path'] = df['path'].map(lambda x : x[3:])
df['path'] = df['path'].map(lambda x : x.split('_'))
#print(df['path'].head())
df = df.explode('path')

process_map = {
    '1' : 'P1',
    '2' : 'P1',
    'V' : 'P2',
    'W' : 'P2',
    'X' : 'P3',
    'Y' : 'P3'
    }

df['process'] = df['path'].map(process_map)
df = df.rename({'path' : 'operator'}, axis = 1)
print(df.head())