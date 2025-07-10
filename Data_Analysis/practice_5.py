# Boolean 추출

import pandas as pd

path = r'C:\Data_Analysis_Study\Data_Analysis\attachment\scientists.csv'
scientists = pd.read_csv(path)
ages = scientists['Age']
'''print(ages.max())
print(ages.mean())

# - 평균 나이보다 나이가 많은 사람의 데이터 추출하기
print(ages > ages.mean())
print(ages[ages > ages.mean()])'''

# BroadCasting
# Series
# Vetor, Scalar
# 같은 길이의 벡터로 더하기, 곱하기 연산은 같은 길이의 벡터가 출력된다.
'''print(ages)
print(ages + ages) #백터 + 백터, 시리즈는 백터의 한 종류이다.
print(ages * ages) #백터 * 백터 
# 벡터와 스칼라 연산을 하면 벡터의 모든 값에 스칼라를 적용하여 브로드캐스팅한다.
print(ages + 100) #백터 + 스칼라
print(ages * 100) #백터 * 스칼라

print(pd.Series[1,100])
print(pd.Series[1,100] + ages)

print(ages.sort_index())
print(ages.sort_index(ascending = False))'''

##########################################################

# DataFrame
# Boolean 추출

'''print(scientists[scientists['Age'] > scientists['Age'].mean()])

# 인덱스가 True인 데이터만 추출
print(scientists.loc[[True,True,False,True,True,False,True,True]])

print(scientists * 2)'''

# Series와 DataFrame의 데이터 처리
# scientists의 Born, Died열의 자료형 확인하고 datetime 자료형으로 변경하여 새로운 변수에 저장
# format 속성을 '%Y-%m-%d'로 지정하여 날짜형식을 만든다.
#print(scientists['Born'].dtype)
#print(scientists['Died'].dtype)

'''Born_series_to_datetime = pd.to_datetime(scientists['Born'], format = '%Y-%m-%d')
Died_series_to_datetime = pd.to_datetime(scientists['Died'], format = '%Y-%m-%d')

(scientists['Born'], scientists['Died']) = (Born_series_to_datetime , Died_series_to_datetime)
print(scientists.head())'''


# 데이터프레임의 행과 열 삭제하기
# 행과 열을 삭제하려면 drop 메소드를 사용해야 한다.
# drop 메소드의 첫 번째 인자는 열 이름, 두 번째 인자에서 axis = 1 은 column의 이름을 의미하고 열을 삭제시키고
# axis = 0 은 인덱스를 의미하고 행을 삭제시킨다.

'''scientists_dropped = scientists.drop(['Age'], axis = 1)
print(scientists_dropped)
print(scientists.index)

scientists_dropped = scientists.drop([1], axis= 0)
print(scientists_dropped.index)
print(scientists_dropped)'''


# 데이터를 저장하고 불러오기
# 피클, CSV, TSV 파일
# 피클은 데이터를 바이너리 형태로 직렬화한 오브젝트를 저장하는 방법이다
# to_pickle 메소드로 저장하고, read_pickle 메소드로 읽어온다.

'''names = scientists['Name']
names.to_pickle(r'C:\Data_Analysis_Study\Data_Analysis\attachment/scientists_names_series.pickle')
scientist_names_from_pickle = pd.read_pickle(r'C:\Data_Analysis_Study\Data_Analysis\attachment/scientists_names_series.pickle')
print(scientist_names_from_pickle)'''


'''scientists.to_pickle(r'C:\Data_Analysis_Study\Data_Analysis\attachment\scientists_df.pickle')
scientists_from_pickle = pd.read_pickle(r'C:\Data_Analysis_Study\Data_Analysis\attachment\scientists_df.pickle')
print(scientists_from_pickle)'''

# CSV 파일과 TSV 파일로 저장하기
# 쉼표로 구분하여 저장한 파일이 CSV파일이고, 탭으로 구분하여 저장한 파일이 TSV이다
# to_csv 메소드
# sep = ‘\t’ 를 추가하면 TSV 파일로도 저장된다.

scientists.to_csv(r'C:\Data_Analysis_Study\Data_Analysis\attachment\scientists_practice.csv') # csv로 저장
scientists.to_csv(r'C:\Data_Analysis_Study\Data_Analysis\attachment\scientists_practice.tsv', sep = '\t') # tsv로 저장
scientists.to_csv(r'C:\Data_Analysis_Study\Data_Analysis\attachment\scientists_practice_no_index', index = False) # index는 저장안함

# series를 xls, xlsx 파일로 저장하기
names_df = names.to_frame()
 
import xlwt 
names_df.to_excel('files/scientists_names_series_df.xls')
 
import openpyxl 
names_df.to_excel('files/scientists_names_series_df.xlsx')