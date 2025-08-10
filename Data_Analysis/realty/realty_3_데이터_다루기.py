from realty_1 import df_last
from realty_1 import df_first
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic') # 한글 인코딩

df_first_melt = df_first.melt(id_vars='지역', var_name='기간', value_name='평당분양가격')
df_first_melt.columns = ['지역명', '기간', '평당분양가격']
#print(df_first.head())


def parse_year(date):
    year = int(date.split('년')[0])
    return year
def parse_month(date):
    month= int(date.split('년')[1].replace('월',''))
    return month

df_first_melt['연도'] = df_first_melt['기간'].apply(parse_year)
df_first_melt['월'] = df_first_melt['기간'].apply(parse_month)
#print(df_first_melt.head())

#print(df_last.columns.to_list())
cols = ['지역명', '연도', '월', '평당분양가격']
df_last_prepare = df_last.loc[df_last['전용면적'] == '전체', cols].copy()
#print(df_last_prepare.sample())

df_first_prepare = df_first_melt[cols].copy()

df = pd.concat([df_first_prepare,df_last_prepare])
#print(df.shape)
