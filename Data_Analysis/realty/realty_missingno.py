import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno


plt.rc('font', family = 'Malgun Gothic') # 한글 인코딩
plt.rc('axes', unicode_minus=False) # xlabel, ylabel 음수의 '-' 인코딩

df = pd.read_csv(r'realty/realty_data/상가업소정보_201912_01.csv', sep='|')
#print(df.shape)

pd.options.display.max_columns = 39
#print(df.head(1))



#### missingno 활용
# msno.heatmap(df)
# plt.show()

# fig, ax = plt.subplots(figsize=(20,10))
# msno.dendrogram(df, ax=ax)
# plt.show()

not_use = df.isna().sum().sort_values(ascending=False).head(9)
not_use_cols = not_use.index
df = df.drop(columns=not_use_cols)

cols = df.columns
cols_code = cols[cols.str.contains('코드|번호')]

df = df.drop(columns=cols_code)