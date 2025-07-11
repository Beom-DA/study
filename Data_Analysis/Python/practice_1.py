import pandas as pd

path = r'C:\Data_Analysis_Study\Data_Analysis\attachment\gapminder.tsv'
df = pd.read_csv(path , sep = '\t') #갭마 데이터는 열이 탭으로 구분되어 있기 때문에 read_csv()를 사용할때 sep속성값을 \t로 지정한다.

#print(df.loc[0]) loc은 행의 'index'를 이용
#print(df.loc[-1]) --> error!! -1은 안됨

#print(df.shape)
number_of_rows = df.shape[0] # 행의 크기
last_row_index = number_of_rows -1 # 마지막 행 인덱스

#print(df.tail(n=2)) # 맨 끝에 두개 행, 반환 자료형은 데이터 프레임

#print(df.iloc[1]) # 데이터 순서를 의미하는 행 번호를 사용하여 데이터를 추출한다.

'''subset = df.loc[:, ['year','pop']] #원하는 열에 해당하는 데이터 추출
print(subset.head())'''

print(df.iloc[0,[2,4,-1]]) # 첫번째 행 2,4,-1 열
print(df.iloc[:,:3]) # 모든 행 0 ~ 2 열
print(df.iloc[:,0:6:2]) # 모든 행 0 ~ 5열 2개씩 띄워서 0 2 4

print(df.iloc[[0, 99, 999], [0, 3, 5]]) #0,99,999행, 0,3,5번째 열
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']]) 
print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])
print(df.iloc[10:13, [0,2,4]])
print(df.groupby('year')['lifeExp'].mean())#year별 lifeExp 열 평균값


