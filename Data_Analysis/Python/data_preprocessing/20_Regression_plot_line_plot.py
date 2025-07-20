####### Regression Plot & Line Plot

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px

df = sns.load_dataset('tips')
#fig, ax = plt.subplots()
#sns.regplot(x='total_bill', y='tip', data = df, ax=ax, ci = None, scatter=False)
#plt.show()

x = np.arange(0,10,1)
y = x**3 - 9*x**2 + x + 4
#sns.regplot(x=x, y=y, ax=ax, order=3,
#            scatter_kws={'s': 80}, line_kws={'color':'red', 'linestyle' : '--'}
#            )
#plt.show()


### plotly로 구현
'''fig = px.scatter(data_frame=df, x='total_bill', y='tip',width=600, height=400,color='smoker', trendline='ols',
                 trendline_scope='overall')
fig.show()'''


### Line plot(Seaborn)
df = pd.read_csv(r'data_analysis_adv/datasets/global_internet_users/global_internet_users.csv')
entities = ['China', 'India', 'Finland']
df = df.query('Entity.isin(@entities)')

'''fig, ax = plt.subplots()
sns.lineplot(
    x='Year', y='No. of Internet Users',
    data=df, ax=ax, hue='Entity', style='Entity'
)
sns.scatterplot(
    x='Year', y='No. of Internet Users',
    data=df, ax=ax, hue='Entity', legend=False
)
plt.show()'''


### Line Plot(plotly)
'''fig = px.line(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=600, height=400, color='Entity'
)'''
#fig.show()

'''fig = px.line(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=600, height=400, line_dash='Entity'
)
fig.show()'''

fig = px.line(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=600, height=400, color = 'Entity', symbol='Entity'
)
fig.show()