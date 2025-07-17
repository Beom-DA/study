import pandas as pd
import numpy as np
import seaborn as sns


####### query 메소드
# 인자로 조건식을나타내는 문자열을 전달하여 행 필터링
# ==, !=, and, or, ~ 사용 가능
# 다양한 문자열 메소드 사용 가능(contains, startswith, endswith)
# @를 사용하여 외부 변수 참조 가능

df = sns.load_dataset('penguins')
'''print(df.query('bill_length_mm > 55'))
print(df.loc[df['bill_length_mm'] > 55])
print(df[df['bill_length_mm'] > 55])'''

df.query('bill_length_mm > 55 and species == "Gentoo')

length = 55
species = 'Gentoo'
df.query('bill_length_mm >= @length and species == @species')

df.query('island.str.contains("oe")', engine = 'python') # island열에서 oe가 포함된 문자열에 해당하는 값들을 추출한다. engine인자는 필수는 아니고 안썼을때 오류가나면 사용한다.
df.query('island.str.endswith("e")')

filtering = ["Adelie", "Chinstrap"]
df.query('species.isin(@filtering)')