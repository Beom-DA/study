import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic') # 한글 인코딩
plt.rc('axes', unicode_minus=False) # xlabel, ylabel 음수의 '-' 인코딩

df = pd.read_csv(r'realty/realty_data/상가업소정보_201912_01.csv', sep='|')
#print(df.shape)

pd.options.display.max_columns = 39
print(df.head(1))