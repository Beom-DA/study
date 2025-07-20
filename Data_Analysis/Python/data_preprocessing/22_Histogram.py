##### Histogram

### Histplot(Matplotlib & Seaborn)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

'''df = sns.load_dataset('tips')
fig, ax = plt.subplots()
sns.histplot(x='total_bill', data=df, ax=ax, bins=30)
#plt.show()

sns.histplot(x='total_bill', data=df, ax=ax, hue='time', multiple='stack')
'''

### Plotly Histogram
df = sns.load_dataset('tips')
'''fig = px.histogram(data_frame=df, x='total_bill',
                   width=500, height=400,
                   nbins=40)
#fig.update_traces(xbins_size = 10) --> 막대 크기를 10으로 한다.
fig.show()'''


'''fig = px.histogram(data_frame=df, x='total_bill',
                   width=500, height=400,
                   color='time', barmode='overlay') # overlay는 겹쳐서 표현

fig = px.histogram(data_frame=df, x='total_bill',
                   width=500, height=400,
                   color='time', barmode='relative') # relative는 seaborn에서 한 multiple='stack'과 같이 위로 쌓아올리는 형식
'''
