####### 조건을 만족하는 최대 연속 횟수 구하기

### 1이 몇번 연속해서 나타나는가?
# cumsum : 누적합
# mul : 곱하기
# diff : f(n) - f(n-1)

# where(조건식, F) : 조건을 만족하는 것은 그대로, 아닌 것은 인자에 전달되는 F 값으로
# ffill : 앞쪽 결측피가 아닌 값을 뒤쪽 결측치에 전파
# add : 더하기

# 문제 : 애플의 주식 종가 기준으로 175불 이상이었던 날짜 중 가장 긴 연속일은?

import pandas as pd
import numpy as np

df = pd.read_csv(r'data_analysis_adv/datasets/APPL_price/APPL_price.csv')
s = df['Close'] > 175
#print(s.sum())

sc = s.cumsum()
s.mul(sc).diff().where(lambda x : x < 0).ffill().add(sc, fill_value = 0).max()
# --> 수학적 트릭이 있기 때문에 다시 공부해보길 바람