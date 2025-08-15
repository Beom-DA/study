import pandas as pd

import numpy as np
df = pd.read_excel("./data/excel-comp-data.xlsx")
df.head()

df["account"].head(2)

df[["account", "street", "state"]].head(3)

df[:10]

df["name"][:3]

account_serires = df["account"]
account_serires[:3]

account_serires[[1,5,2]]

account_serires[account_serires<250000]

df.index = df["account"]
df.head()

del df["account"]
df.head()

df[["name","street"]][:2]


df.loc[[211829,320563],["name","street"]]


df[["name", "street"]].iloc[:10]

df.index = list(range(0,15))
df.head()


df.drop(1)


df.drop([0,1, 2,3])

matrix = df.as_matrix()
matrix[:3]

matrix[:,-3:]
matrix[:,-3:].sum(axis=1)
df.drop("city",axis=1).head()


df.drop(["city", "state"],axis=1)
matrix = df.as_matrix()
matrix