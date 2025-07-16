import pandas as pd
import numpy as np

df = pd.read_csv(r'./datasets/bike_rentals/bike_rentals.csv')

####### info 메소드
# dataframe의 정보 확인(길이, 열 ,데이터 타입, 크기 등)

####### select_dtype 메소드
# include 인자 : 특정 데이터 타입을 가지는 열만 필터링 ex) df.select_dtypes(include = 'int')
# exclude 인자 : 특정 데이터 타입을 가지는 열만 제외   ex) df.select_dtypes(exclude = 'int')

####### filter 메소드
# like 인자 : 전달된 값을 포함하는 행/열만 필터링
# items 인자 : 전달된 값에 해당하는 행/열만 필터링 --> 잘 쓰이지 않음
# regex 인자 : 정규 표현식을 통한 행/열 필터링 ex) df.filter(regex='in.s') --> 열의 이름 중에 in과 s 사이에 하나의 문자열이 들어가있는 이름 --> windspeed
# axis 인자 : 0은 행, 1은 열을 뜻함(기본값 1)
# ex)
'''df = df.set_index('datetime') # index가 int에서 datetime으로 바뀐다.
df = df.filter(like = '00:00:00', axis = 0)
print(df)'''


####### rename 메소드
# 변경하기 위한 인덱스/열 이름을 {변경전 : 변경후} 딕셔너리로 전달
# axis 인자 : 0은 행, 1은 열을 뜻함(기본값 0)
# axis 인자 대신 colums, index 인자 사용 가능
#ex) 열의 이름을 바꾸는 똑같은 방식
df = df.rename(
    {'registered' : 'registered_user',
     'casual' : 'unregistered_user'}, axis = 1
)
df = df.rename(
    columns={'registered' : 'registered_user',
     'casual' : 'unregistered_user'}
)

