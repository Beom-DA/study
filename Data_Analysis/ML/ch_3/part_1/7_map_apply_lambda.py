import pandas as pd
import numpy as np
from pandas import Series

f = lambda x,y: x + y
f(1,4)
def f(x , y):
    return x + y
f = lambda x: x ** 2
f(3)
f = lambda x: x+5
f(3)
(lambda x: x +1)(5)



ex = [1,2,3,4,5]
f = lambda x: x ** 2
list(map(f, ex))
f = lambda x, y: x + y
list(map(f, ex, ex))
list(map(lambda x: x+5, ex)) 
#python 3에는 list를 꼭 붙여줘야함
s1 = Series(np.arange(10))
s1.head(5)

s1.map(lambda x: x**2).head(5)

z = {1: 'A', 2: 'B', 3: 'C'}
s1.map(z)

s2 = Series(np.arange(10,20))
s1.map(s2)



#df = pd.read_csv("./data/wages.csv")
df = pd.read_csv(r'wages.csv')
print(df.head())

df.sex.unique()

df["sex_code"] =  df.sex.map({"male":0, "female":1})
df.head(5)

df.sex.replace(
    {"male":0, "female":1}
).head()

df.sex.head(5)
df.sex.replace(
    ["male", "female"], 
    [0,1], inplace=True)

del df["sex_code"]
df.head()






df = pd.read_csv("wages.csv")
df.head()
df_info = df[["earn", "height","age"]]
df_info.head()
f = lambda x : x.max() - x.min()
df_info.apply(f)
df_info.apply(sum)
df_info.sum()
def f(x):
    return Series([x.min(), x.max(), x.mean()], 
                    index=["min", "max", "mean"])
df_info.apply(f)
f = lambda x : -x
df_info.applymap(f).head(5)
f = lambda x : -x
df_info["earn"].apply(f).head(5)