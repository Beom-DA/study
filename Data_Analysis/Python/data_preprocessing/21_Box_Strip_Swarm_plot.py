### Box Plot
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('tips')
'''fig, ax = plt.subplots(figsize=(3,4))
sns.boxenplot(y='total_bill', data=df, ax = ax)
plt.show()
'''
'''df = pd.read_csv(r'data_analysis_adv/datasets/EV_charge/EV_charge.csv')
fig, ax = plt.subplots()
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax)
plt.show()'''

### Stripplot & SwarmPlot
'''df = pd.read_csv(r'data_analysis_adv/datasets/EV_charge/EV_charge.csv')
fig, ax = plt.subplots()
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax)
sns.stripplot(x='weekday', y='kwhTotal', data=df, ax=ax,
              color='grey', alpha = 0.4)
plt.show()'''

'''df = pd.read_csv(r'data_analysis_adv/datasets/EV_charge/EV_charge.csv')
fig, ax = plt.subplots()
weekday_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax,order = weekday_order)
sns.swarmplot(x='weekday', y='kwhTotal', data=df, ax=ax,
              color='grey', alpha = 0.4,
              order = weekday_order) # alpha는 투명도 조절
plt.show()'''

'''df = pd.read_csv(r'data_analysis_adv/datasets/EV_charge/EV_charge.csv')
fig, ax = plt.subplots()
weekday_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sns.boxenplot(x='weekday', y='kwhTotal', data=df, ax=ax,order = weekday_order,
              hue='platform')
plt.show()'''


### boxplot (plotly로 그리기)
import plotly.express as px
weekday_order = {
    'weekday': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    } # 딕셔너리 이용(key값 = x에 해당하는 변수 값)
df = pd.read_csv(r'data_analysis_adv/datasets/EV_charge/EV_charge.csv')
fig = px.box(data_frame=df, x='weekday', y='kwhTotal', 
             width=500, height=400, hover_data=['platform'], points = 'all',
             category_orders=weekday_order, color='platform')
fig.show()