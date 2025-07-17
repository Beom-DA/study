import pandas as pd
import numpy as np
import seaborn as sns

####### 시계열 데이터
# 시간에 따라 변화하는 특성을 가지거나, 분석의 기준이 시간이 되는 경우
# 시계열 행 슬라이싱 사용 가능
# 특정 시간 단위로 묶어 연산을 수행하는 resample 메소드 사용 가능
df = pd.read_csv(r'data_analysis_adv/datasets/APPL_price/APPL_price.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 슬라이싱
'''df['1980-12-13' : '1980-12-18']
df['2015-02' : '2015-02']'''

# resample 메소드
#d datetime 데이터형이 인덱스인 경우 특정 날짜/시간 단위로 데이터 분절 후 연산 가능
# offset string을 인자로 전달하여 그룹화 할 날짜/시간 단위 설정
# closed, label 인자 등 사용 가능
df = df.resample('7d').mean()
