import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
import matplotlib.transforms as transforms

### Color Palette 및 Color Map 활용(Matplotlib & Seaborn)
# df = sns.load_dataset('tips')

# fig, ax = plt.subplots()
# 1.
# sns.scatterplot(
#     data=df, x='total_bill', y='tip', ax=ax,
#     hue='size', palette='bright' # 'colorblind'
# )

# 2.
# sns.scatterplot(
#     data=df, x='total_bill', y='tip', ax=ax,
#     hue='day',
#     hue_order=['Thur','Fri','Sat','Sun'],
#     palette=['black','cyan','purple','salmon']
# )

# 3.
# sns.scatterplot(
#     data=df, x='total_bill', y='tip', ax=ax,
#     hue='day',
#     palette={'Thur':'black','Fri':'cyan','Sat':'purple','Sun':'salmon'}
# )

# 4.
# color = sns.color_palette('coolwarm', as_cmap=True) # as_cmap=True를 추가하면 반환형이 연속형 컬러맵 객체가 된다.
# sns.scatterplot(
#     data=df, x='total_bill', y='tip', ax=ax,
#     hue='size',
#     palette=color
# )

# 5.
# color = sns.color_palette('light:#006d2c', as_cmap=True) # as_cmap=True를 추가하면 반환형이 연속형 컬러맵 객체가 된다.
# sns.scatterplot(
#     data=df, x='total_bill', y='tip', ax=ax,
#     hue='size',
#     palette=color
# )

# 6.
# sns.scatterplot(
#     data=df, x='total_bill', y='tip', ax=ax,
#     hue='day',
#     palette={'Thur':'#808000','Fri':'#0000FF','Sat':'#DDA0DD','Sun':'#8bf90f'}
# )



## heatmap

# df = sns.load_dataset('diamonds')
# pivot = df.pivot_table(index='color', columns='clarity',
#                     values='price')
# clarity_order = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

# fig, ax = plt.subplots(figsize=(8,6))
# 1.
# sns.heatmap(
#     data=pivot[clarity_order], annot=True, fmt='.0f'
# )

# 2.
# sns.heatmap(
#     data=pivot[clarity_order], annot=True, fmt='.0f',
#     cmap=['black', 'darkgrey', 'lightgrey', 'white'] # 색깔 범위 지정
# )

# 3.(활용) color map 직접 만들어서 사용하기
# from matplotlib.colors import LinearSegmentedColormap

# color = LinearSegmentedColormap.from_list(
#     'custom color', # 임의의 이름
#     [(0, '#ffffff'), (0.5, '#ffffff'), (1, '#0000ff')], # 0 은 맨 아래, 0.5는 중간, 1은 맨위
#     N=256 # 0~1 사이의 색깔 범위를 256등분 하겠다.
# )
# sns.heatmap(
#     data=pivot[clarity_order], annot=True, fmt='.0f',
#     linewidths=0.5, linecolor='black', cmap=color
# )

# plt.show()




### Color Palette 및 Color Map 활용(Plotly)

# plotly에서 제공하는 색
# fig = px.colors.qualitative.swatches()
# fig.show()
# fig = px.colors.sequential.swatches_continuous()
# fig.show()
# fig = px.colors.diverging.swatches_continuous()
# fig.show()
# fig = px.colors.cyclical.swatches_continuous()
# fig.show()


df = sns.load_dataset('tips')
# 1. 
# fig = px.scatter(
#     data_frame=df, x='total_bill', y='tip',width=500, height=400,
#     color='size', color_continuous_scale='balance'
# )

# 2.
# fig = px.scatter(
#     data_frame=df, x='total_bill', y='tip',width=500, height=400,
#     color='day', color_discrete_sequence=px.colors.qualitative.Light24
# )

# 3.
# fig = px.scatter(
#     data_frame=df, x='total_bill', y='tip',width=500, height=400,
#     color='day', color_discrete_sequence=[
#         'rgb(255,255,255)',
#         'rgb(0,0,0)',
#         'rgb(128,128,128)',
#         'rgb(64,255,192)'
#     ]
# )

# 4.
# fig = px.scatter(
#     data_frame=df, x='total_bill', y='tip',width=500, height=400,
#     color='day', color_discrete_map={
#         'Thur':'black','Fri':'cyan','Sat':'purple','Sun':'salmon'
#     }
# )

# 5. heatmap
# df = sns.load_dataset('diamonds')
# pivot = df.pivot_table(index='color', columns='clarity',
#                     values='price')
# clarity_order = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
# colors = ['black', 'darkgrey', 'lightgrey', 'white']
# fig = px.imshow(
#     pivot[clarity_order], width=500, height=400, text_auto='4d', #4d는 정수 4개
#     color_continuous_scale=colors
# )

# 6. (활용) color map 직접 만들어서 사용하기
df = sns.load_dataset('diamonds')
pivot = df.pivot_table(index='color', columns='clarity',
                    values='price')
clarity_order = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

fig = px.imshow(
    pivot[clarity_order], width=500, height=400, text_auto='4d'
)

fig.update_coloraxes(
    showscale=True,
    colorscale=[
        (0, '#ffffff'), (0.5, '#ffffff'), (1, '#0000ff')
    ]
)
fig.show()