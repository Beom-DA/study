import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
import matplotlib.transforms as transforms

'''### FacetGrid에서 특정 조건에 해당하는 ax 강조하기(Matplotlib & Seaborn)
df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])


#★ 함수를 통해 수평선을 그리고 이상치가 있는 ax를 표시하는 방법
def custom(value, lower_spec, target, upper_spec, **kws):
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

def if_spec_out(spec_out, **kws):
    if spec_out.sum() > 0 :
        ax = plt.gca()
        spines = ['left', 'bottom']
        for spine in spines:
            ax.spines[spine].set_color('blue')
            ax.spines[spine].set_linewidth(3)


df['spec_out'] = (df['value'] > df['upper_spec']) | (df['value'] < df['lower_spec'])

g = sns.FacetGrid(
    df, sharex=False, sharey=False, col='inspection_step',aspect=1.6
) # 도화지를 그리고

g.map_dataframe(sns.scatterplot, x= 'date', y='value')
# 어떤 그래프를 그릴지 정하고, 데이터를 넣는다

g.map(custom, 'value', 'lower_spec', 'target', 'upper_spec')
# # 수평선을 넣고

g.map(if_spec_out, 'spec_out')
# # 이상치가 있는 ax 를 표시한다.

plt.show()'''








#★ for문을 통해 수평선을 그리고 이상치를 표시하는 방법
'''df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])

df['spec_out'] = (df['value'] > df['upper_spec']) | (df['value'] < df['lower_spec'])

g = sns.FacetGrid(
    df, sharex=False, sharey=False, col='inspection_step',aspect=1.6
)

g.map_dataframe(sns.scatterplot, x= 'date', y='value')

for ax in g.axes.flat:
    title = ax.get_title()[-1] # ex) get_title의 값이 'inspection_step=A'이기에 A라는 값을 가져오기 위한 코드
    temp_df = df.query('inspection_step == @title')

    ax.axhline(temp_df['lower_spec'].iloc[-1], color='red', linewidth=0.5)
    ax.axhline(temp_df['target'].iloc[-1], color='red', linewidth=0.5)
    ax.axhline(temp_df['upper_spec'].iloc[-1], color='red', linewidth=0.5)

    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

    spec_out_df = temp_df.query('spec_out != 0')
    if len(spec_out_df) > 0:
        for idx in range(len(spec_out_df)):
            ax.annotate(
            xy = (spec_out_df.iloc[idx]['date'], spec_out_df.iloc[idx]['value']),
            xytext = (spec_out_df.iloc[idx]['date'], spec_out_df.iloc[idx]['value'] * 1.03),
            text = 'spec out', arrowprops={'color': 'red', 'width' : 2}, color = 'black', weight='bold'
        )

plt.show()'''



### FacetGrid에서 특정 조건에 해당하는 ax 강조하기(Plotly)
df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')

df['spec_out'] = (df['value'] > df['upper_spec']) | (df['value'] < df['lower_spec'])

fig = px.scatter(
    data_frame=df, x='date', y='value', facet_col='inspection_step', facet_col_spacing=0.05
)

for idx in range(df['inspection_step'].nunique()):
    step = fig.layout.annotations[idx].text.split('=')[1]
    fig.add_hline(
        y=df.query('inspection_step == @step')['lower_spec'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )
    fig.add_hline(
        y=df.query('inspection_step == @step')['upper_spec'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )
    fig.add_hline(
        y=df.query('inspection_step == @step')['target'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )

    if df.query('inspection_step == @step')['spec_out'].sum() > 0:
        fig.update_xaxes(showline=True, linecolor='black', linewidth=3, mirror=False, row=1, col = idx+1)
        fig.update_yaxes(showline=True, linecolor='black', linewidth=3, mirror=False, row=1, col = idx+1)

    
    spec_out_df = df.query('inspection_step == @step and spec_out > 0')

    if len(spec_out_df) > 0:
        for jdx in range(len(spec_out_df)):
            fig.add_annotation(
                text='spec_out',
                x=spec_out_df.iloc[jdx]['date'],
                y=spec_out_df.iloc[jdx]['value'],
                row=1, col=idx+1, arrowcolor='red',
                font={'color' : 'red', 'size' : 20}
            )

fig.update_yaxes(matches=None, showticklabels=True)
fig.show()