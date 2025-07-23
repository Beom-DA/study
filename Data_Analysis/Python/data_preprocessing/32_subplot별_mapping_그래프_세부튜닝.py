import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
import matplotlib.transforms as transforms

### Seaborn FacetGrid를 통해 그린 subplot들을 각 그룹별 통계값으로 튜닝하기
'''df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])

g = sns.FacetGrid(df, sharex = False, sharey = False, col ='inspection_step', aspect= 1.6) # aspect는 세로대비 가로 비율, 가로가 세로의 1.6배
g.map_dataframe(sns.scatterplot, x='date', y='value')'''

'''# 사용자 정의함수
def custom(lower_spec, target, upper_spec, **kws):
    ax = plt.gca()#get current ax의 약자

    ax.axhline(lower_spec.iloc[-1], color = 'red', linewidth=0.5)
    ax.axhline(target.iloc[-1], color = 'red', linewidth=0.5)
    ax.axhline(upper_spec.iloc[-1], color = 'red', linewidth=0.5)

    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

g.map(custom, 'lower_spec', 'target', 'upper_spec')
plt.show()'''

'''#for문
for ax in g.axes.flat:
    inspection_step = ax.get_title()[-1]
    temp_df = df.loc[df['inspection_step'] == inspection_step]

    ax.axhline(temp_df['lower_spec'].iloc[-1], color = 'red', linewidth=0.5)
    ax.axhline(temp_df['target'].iloc[-1], color = 'red', linewidth=0.5)
    ax.axhline(temp_df['upper_spec'].iloc[-1], color = 'red', linewidth=0.5)

    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

plt.show()'''



# target에 해당하는 수평선에 대한 mean값 기입
# 사용자 정의함수
'''def custom(value, lower_spec, target, upper_spec, **kws):
    ax = plt.gca()#get current ax의 약자

    ax.axhline(lower_spec.iloc[-1], color = 'red', linewidth=0.5)
    ax.axhline(target.iloc[-1], color = 'red', linewidth=0.5)
    ax.axhline(upper_spec.iloc[-1], color = 'red', linewidth=0.5)

    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

    # target에 해당하는 수평선에 대한 mean값 기입
    mean = value.mean()
    ax.axhline(mean , color='blue', linestyle = '--', linewidth = 2)
    # 심화과정으로 각 subplot 별 데이터 media 값 표시
    trans = transforms.blended_transform_factory(ax.transAxes, ax.transData)
    ax.text(
        x= 0.02, y= mean, s='mean : {:.1f}'.format(mean),
        fontdict={'fontsize' : 12, 'weight' : 'bold'}, bbox = {'facecolor':'white'},
        transform=trans, ha = 'left'
    )

g.map(custom, 'value', 'lower_spec', 'target', 'upper_spec')
plt.show()'''



### Plotly facet을 통해 그린 subplot들을 각 그룹별 통계값으로 튜닝하기
df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')

fig = px.scatter(
    data_frame=df, x='date', y='value', facet_col='inspection_step', facet_col_spacing=0.05
)
#print(fig.layout.annotations[0].text)

for idx in range(df['inspection_step'].nunique()):
    step = fig.layout.annotations[idx].text.split('=')[1]

    fig.add_hline(
        y=df.query('inspection_step == @step')['lower_spec'].iloc[-1],
        line_color = 'red', line_width=0.5, row=1, col = idx + 1
    )

    fig.add_hline(
        y=df.query('inspection_step == @step')['upper_spec'].iloc[-1],
        line_color = 'red', line_width=0.5, row=1, col = idx + 1
    )

    fig.add_hline(
        y=df.query('inspection_step == @step')['target'].iloc[-1],
        line_color = 'red', line_width=0.5, row=1, col = idx + 1
    )

    med = df.query('inspection_step == @step')['value'].median()
    fig.add_hline(
        y=med,
        line_color = 'black', line_width=3, line_dash = 'dot',
        row=1, col = idx + 1
    )
    fig.add_annotation(
        text = 'median : {:.1f}'.format(med),
        showarrow=False, bordercolor='black', borderwidth=1,
        bgcolor='rgb(256,256,256)',
        x=0.02, y=med, xref='x domain',# x값은 상대좌표기 때문에 xref가 필요하고  y좌표는 절대좌표기 떄문에 yref가 필요없다.
        row=1, col=idx+1
    )
fig.update_yaxes(matches=None, showticklabels=True)# y축의 범위를 서로 다르게 사용하겠다
fig.show()