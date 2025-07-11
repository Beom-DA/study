# 시리즈의 기초 통계 메소드 사용하기
# 시리즈의 mean, min, max, std 메소드 사용하기
# scientists의 age열을 추출한다.

import pandas as pd
from collections import OrderedDict

scientists = pd.DataFrame(OrderedDict([ 
    ('Name', ['Rosaline Franklin', 'William Gosset']),
    ('Occupation', ['Chemist', 'Statistician']), 
    ('Born', ['1920-07-25', '1876-06-13']), 
    ('Died', ['1958-04-16', '1937-10-16']), 
    ('Age', [37, 61])
])
) 

ages = scientists['Age']
print(type(ages))
print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std()) #표준편차