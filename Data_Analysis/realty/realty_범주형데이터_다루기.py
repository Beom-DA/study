from realty_missingno import df
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_object = df.describe(include='object')
#print(df_object)

df_seoul_food = df.loc[(df['시도명'] == '서울특별시') & (df['상권업종대분류명'] == '음식')].copy()
#print(df_seoul_food.head(1))

food_gu  = df_seoul_food.groupby(['시군구명', '상권업종중분류명'])['상호명'].count()
#print(food_gu)

food = food_gu.reset_index()
food = food.rename(columns={'상호명' : '상호개수'})
print(food)