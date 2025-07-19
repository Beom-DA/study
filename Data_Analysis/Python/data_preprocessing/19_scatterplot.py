####### scatterplot

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r'data_analysis_adv/datasets/global_internet_users/global_internet_users.csv')
#print(df)
#fig, ax = plt.subplots()

'''sns.scatterplot(x = 'Year', y = 'No. of Internet Users', data = df, ax = ax)
plt.show()'''


# Entitiy 변수에서 일부만 사용하기 위해 고유값 확인
df.Entity.unique()

# Entity 3가지 값들로만 필터링 하여 사용
entities = ['China', 'India', 'Finland']
df = df.loc[df['Entity'].isin(entities)]
#df = df.query('Entity.isin(@entities)') 위 코드와 똑같은 코드
fig, ax = plt.subplots()
#sns.scatterplot(x='Year', y = 'No. of Internet Users', data = df, ax = ax, hue = 'Entity', palette = 'bright')
#plt.show()

# hue_order
sns.scatterplot(x='Year', y = 'No. of Internet Users', data = df, ax = ax, hue = 'Entity', hue_order = ['India', 'Finland', 'China'], palette = 'bright')
#plt.show()

#stlye 인자의 활용
sns.scatterplot(x='Year', y = 'No. of Internet Users', data = df, ax = ax, style = 'Entity', markers=['o', '^', 'X'], s = 100)
#plt.show()

# size, sizes 인자 활용
sns.scatterplot(x='Year', y = 'No. of Internet Users', data = df, ax = ax, size = 'Entity', sizes = (40, 200))
plt.show()