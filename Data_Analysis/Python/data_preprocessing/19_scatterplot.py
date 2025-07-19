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
#fig, ax = plt.subplots()
#sns.scatterplot(x='Year', y = 'No. of Internet Users', data = df, ax = ax, hue = 'Entity', palette = 'bright')
#plt.show()

# hue_order
#sns.scatterplot(x='Year', y = 'No. of Internet Users', data = df, ax = ax, hue = 'Entity', hue_order = ['India', 'Finland', 'China'], palette = 'bright')
#plt.show()

#stlye 인자의 활용
#sns.scatterplot(x='Year', y = 'No. of Internet Users', data = df, ax = ax, style = 'Entity', markers=['o', '^', 'X'], s = 100)
#plt.show()

# size, sizes 인자 활용
#sns.scatterplot(x='Year', y = 'No. of Internet Users', data = df, ax = ax, size = 'Entity', sizes = (40, 200))
#plt.show()

# seaborn scatterplot 활용
'''df = sns.load_dataset('tips')
fig, ax = plt.subplots()
sns.scatterplot(x = 'total_bill', y = 'tip', data = df, ax = ax, hue = 'smoker', style = 'time', size = 'size')
plt.show()'''

####### Plotly로 scatterplot 그리기
import plotly.express as px

'''fig = px.scatter(
    data_frame = df, x = 'Year', y = 'No. of Internet Users',
    width = 400, height=400, hover_data=['Entity']
)
fig.show()'''


### color 인자 활용
'''fig = px.scatter(
    data_frame=df, x = 'Year', y = 'No. of Internet Users',
    width = 400, height=400, color='Entity'
)
fig.show()'''

# color_discrete_sequence 이용
'''fig = px.scatter(
    data_frame=df, x = 'Year', y = 'No. of Internet Users',
    width = 400, height=400, color='Entity',
    # color_discrete_sequence=['blue','black','red']
    color_discrete_sequence=px.colors.qualitative.Light24
)
fig.show()'''

# color_discrete_map 이용
'''fig = px.scatter(
    data_frame=df, x = 'Year', y = 'No. of Internet Users',
    width = 400, height=400, color='Entity',
    color_discrete_map={'China' : 'blue', 'Finland' : 'black', 'India' : 'red'}
)
fig.show()'''


### symbol 인자의 활용
'''fig = px.scatter(
    data_frame=df, x = 'Year', y = 'No. of Internet Users',
    width = 400, height=400, symbol='Entity',
    symbol_sequence=['star', 'arrow', 'cross']
)
fig.show()'''


### size 인자의 활용
'''fig = px.scatter(
    data_frame=df, x = 'Year', y = 'No. of Internet Users',
    width = 400, height=400, size = 'No. of Internet Users'
)
fig.show()'''

### Plotly scatter 활용
df = sns.load_dataset('tips')
fig = px.scatter(
    data_frame=df, x = 'total_bill', y = 'tip',
    width = 600, height=400,
    color='smoker', size = 'size', symbol = 'time'
)
fig.show()

