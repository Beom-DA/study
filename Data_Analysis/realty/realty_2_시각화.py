from realty_1 import df_last
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font', family = 'Malgun Gothic') # 한글 인코딩

# g = df_last.groupby(['지역명'])['평당분양가격'].mean()
# g.plot(kind='bar') # g.plot.bar(rot = 0) rot인자는 누워있는 글자를 바로 세우는 인자(rotation)
# plt.show()

# g = df_last.groupby(['연도'])['평당분양가격'].mean()
# g.plot.bar()
# plt.show()

# g = df_last.pivot_table(index = '월', columns=['연도','전용면적'], values='평당분양가격')
# g.plot.box(figsize = (15,3), rot=30)
# plt.show()


#### distplot
# .loc[행]
# .loc[행,열]
# price = df_last.loc[df_last['평당분양가격'].notnull(),'평당분양가격']
# sns.distplot(price)
# plt.show()


#### ridge plot
# g = sns.FacetGrid(df_last, row='지역명',
#                   height=1.7, aspect=4)
# g.map(sns.distplot, '평당분양가격', hist=False, rug = True)
# plt.show()


#### pair plot
# df_last_not_null = df_last.loc[df_last['평당분양가격'].notnull(),
#                            ['연도', '월', '평당분양가격', '지역명', '전용면적']]
# sns.pairplot(df_last_not_null, hue='전용면적')
# plt.show()


#### lmplot
# sns.lmplot(data=df_last, x='연도', y='평당분양가격')
# plt.show()



#### swarmplot
# sns.swarmplot(data=df_last, x='연도', y='평당분양가격', hue='지역명')
# plt.legend(bbox_to_anchor=(1.02, 1), loc = 2, borderaxespad=0.)
# plt.show()

#### violin plot
sns.violinplot(data=df_last, x='연도', y='평당분양가격')
plt.legend(bbox_to_anchor=(1.02, 1), loc = 2, borderaxespad=0.)
plt.show()