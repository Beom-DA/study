####### groupby 메소드를 이용한 문자열 연산

### groupby의 문자열 연산
# 문자열의 더하기(이어쓰기)를 이용한 groupby 연산 수행 가능

import pandas as pd
import numpy as np

df = pd.read_csv(r'data_analysis_adv/datasets/product/product.csv')
df['path'] = df.groupby('product_id')['operator'].transform(lambda x : '_'.join(x))
#print(df['path'])

df['path'] = df['factory'] + '_' + df['path']
df = df.drop_duplicates('product_id')
df = df[['date', 'product_id', 'passfail', 'path']]


# 특정 공정과 pass/fail 간의 연관성이 있는지 확인
# path 별로 pass/fail의 value_counts 실행
df.groupby('passfail')['path'].value_counts()

# date 별로 pass/fail의 value_counts 실해
df.groupby('passfail')['date'].value_counts()