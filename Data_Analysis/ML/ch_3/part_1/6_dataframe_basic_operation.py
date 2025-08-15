import pandas as pd
from pandas import Series
from pandas import DataFrame
import numpy as np



s1 = Series(
    range(1,6), index=list("abced"))
s1
s2 = Series(
    range(5,11), index=list("bcedef"))
s2
s1 + s2
s1.add(s2)


df1 = DataFrame(
    np.arange(9).reshape(3,3), 
    columns=list("abc"))
df1
df2 = DataFrame(
    np.arange(16).reshape(4,4), 
    columns=list("abcd"))
df2
df1 + df2
df1.add(df2,fill_value=0)


df = DataFrame(
    np.arange(16).reshape(4,4), 
    columns=list("abcd"))
df
s = Series(
    np.arange(10,14), 
    index=list("abcd"))
s
df + s
s2 = Series(np.arange(10,14))
s2
df
df + s2
df.add(s2, axis=0)