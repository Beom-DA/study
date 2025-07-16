import pandas as pd
import numpy as np

df = pd.read_csv(r'./datasets/bike_rentals/bike_rentals.csv')
df.iloc[2, 3] = np.nan # nan 은 numpy에서 결측치로 구분하는 값
###### iloc 메소드
# 행과 열을 숫자 인덱스로 선택
# 슬라이싱 가능 ex) df.iloc[2:5, 3:6] --> 인덱스로 선택하기 때문에 맨 뒤 인덱스는 미포함

###### loc 메소드
# 행과 열을 인덱스 이름으로 선택
# loc[행 이름, 열 이름]
# 슬라이싱 가능 ex) df.loc[2:4, 'workingday':'temp'] --> 인덱스의 이름으로 선택하기 때문에 맨 뒤 열 포함
# print(df.loc[2:4, 'workingday':'temp'])

# loc[조건문] 형태로 조건을 만족하는 행 필터링 가능 ex) df.loc[df['season'] == 2]
# 열까지 선택하려면 loc[조건문, 열 이름] 형식으로 사용 ex) df.loc[df['season'] == 2, 'casual' :] --> searson열의 값이 2인 행들을 고르되 casual 열부터 끝까지 출력

# loc 메소드 조건문 활용
# &(and), |(or), !=(not equal), ~(not)
