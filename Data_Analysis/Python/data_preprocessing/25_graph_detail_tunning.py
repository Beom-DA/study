### 그래프 세부 요소 튜닝하기

# Matplotlib tick label 회전, 글씨 크기 조절
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

'''df = pd.read_csv(r'data_analysis_adv/datasets/ds_salaries/ds_salaries.csv')
companies = df['company_location'].unique()[0:30]
#companies = df.company_location.unique()[0:30] 두개가 똑같은 코드
df_30companies = df.loc[df['company_location'].isin(companies)]'''
'''
fix, ax = plt.subplots()
sns.boxenplot(
    x='company_location', y='salary_in_usd',
    data=df_30companies, ax=ax
)
#ax.tick_params(axis='x', labelrotation=90)
plt.show()'''


### Plotly tick label 회전, 글씨 크기 조절
'''fig = px.box(
    data_frame=df_30companies, x='company_location',y='salary_in_usd',
    width=700, height=500
).update_xaxes(tickfont={'size' : 16}, tickangle = -90)
fig.show()'''


### Matplotlib 그래프 제목 입력
'''df = pd.read_csv(r'data_analysis_adv/datasets/ds_salaries/ds_salaries.csv')

fig, ax = plt.subplots(1,3, figsize=(15,5))

sns.boxplot(
    x='company_size', y='salary_in_usd', data=df, ax=ax[0],
    order=['S','M','L']
)
ax[0].set_title('company_size box plot', fontsize = 16)

sns.histplot(
    x='salary_in_usd', data=df, ax=ax[1]
)
ax[1].set_title('salary histogram', fontsize = 16)

pivot_df = df.pivot_table(
    index='company_size', columns='experience_level', values= 'salary_in_usd', aggfunc='mean'
)
sns.heatmap(pivot_df, ax=ax[2], annot=True)
ax[2].set_title('heatmap of\nexperience_level X company_size', fontsize =16)
plt.show()'''



### Plotly 그래프 제목 입력
'''df = pd.read_csv(r'data_analysis_adv/datasets/ds_salaries/ds_salaries.csv')
order_list = ['S','M','L']
fig = px.box(
    data_frame=df, x='company_size', y='salary_in_usd',
    width=400, height=400,
    title='<b>company_size box plot</b>',
    category_orders={'company_size': order_list}
)
fig.update_layout({'title_font_size' : 20})
fig.show()'''


### Grid (Matplotlib & Seaborn)
'''df = pd.read_csv(r'data_analysis_adv/datasets/ds_salaries/ds_salaries.csv')

fig, ax = plt.subplots()
sns.boxplot(
    data=df, x='company_size', y='salary_in_usd',
    ax=ax, hue='company_size'
)
ax.set_title('company_size box plot', fontsize = 12)
ax.grid(axis='y') # axis='both'도 가능
plt.show()'''


### Grid (Plotly)
# grid 제거법
'''df = pd.read_csv(r'data_analysis_adv/datasets/ds_salaries/ds_salaries.csv')

fig = px.box(
    data_frame=df, x='company_size', y='salary_in_usd',
    width=700, height=500
)
fig.update_layout(yaxis={'showgrid':False})
fig.show()'''


### Subplot 위치 조절(Matplotlib & Seaborn)
'''df = pd.read_csv(r'data_analysis_adv/datasets/ds_salaries/ds_salaries.csv')

fig, ax = plt.subplots(2,2)
for idx in range(2):
    for jdx in range(2):
        ax[idx][jdx].set_xlabel('x_label')
        ax[idx][jdx].set_ylabel('y_label')
        ax[idx][jdx].set_title('title')

plt.tight_layout() # 서로 겹치지 않게 자동 설정
# plt.tight_layout(
#     pad=5, w_pad=1,h_pad=4
# )
# plt.tight_layout(
#     rect=(0.5,0,1,1)
# )
plt.show()'''


### Subplot 위치 조절(Plotly)
df = sns.load_dataset('tips')

fig = px.scatter(
    data_frame=df, x='total_bill', y='tip',
    facet_row='sex', facet_col='time',
    width=500, height=500,
    facet_row_spacing=0.2, facet_col_spacing=0.1
)
fig.show()