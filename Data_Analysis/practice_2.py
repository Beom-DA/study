# 기초적인 통계 계산하기
# lifeExp 열을 연도별로 그룹화하여 평균 계산하기

import pandas as pd

path = r'C:\Data_Analysis_Study\Data_Analysis\attachment\gapminder.tsv'
df = pd.read_csv(path, sep = '\t')

#mean_data_of_exp = df.groupby('year')['lifeExp'].mean()
#print(mean_data_of_exp)

'''mean_data = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(mean_data)'''


##### 그래프 그리기

import matplotlib.pyplot as plt

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
#print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()
plt.show()