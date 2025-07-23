import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
import matplotlib.transforms as transforms

### FacetGrid에서 특정 조건에 해당하는 ax 강조하기(Matplotlib & Seaborn)
df = pd.read_csv(r'data_analysis_adv/datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])

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
)
g.map_dataframe(sns.scatterplot, x= 'date', y='value')

g.map(custom, 'value', 'lower_spec', 'target', 'upper_spec')

g.map(if_spec_out, 'spec_out')

plt.show()