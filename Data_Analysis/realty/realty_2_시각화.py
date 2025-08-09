from realty_1 import df_last
import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic') # 한글 인코딩

# g = df_last.groupby(['지역명'])['평당분양가격'].mean()
# g.plot(kind='bar') # g.plot.bar(rot = 0) rot인자는 누워있는 글자를 바로 세우는 인자(rotation)
# plt.show()

# g = df_last.groupby(['연도'])['평당분양가격'].mean()
# g.plot.bar()
# plt.show()

g = df_last.pivot_table(index = '월', columns=['연도','전용면적'], values='평당분양가격')
g.plot.box(figsize = (15,3), rot=30)
plt.show()