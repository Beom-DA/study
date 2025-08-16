import pandas as pd
import numpy as np
# Eaxmple from - https://chrisalbon.com/python/pandas_missing_data.html
raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
        'age': [42, np.nan, 36, 24, 73],
        'sex': ['m', np.nan, 'f', 'm', 'f'],
        'preTestScore': [4, np.nan, np.nan, 2, 3],
        'postTestScore': [25, np.nan, np.nan, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])


df.isnull().sum() / len(df)

df_no_missing = df.dropna()

df_cleaned = df.dropna(how='all')

df['location'] = np.nan

df.dropna(axis=1, how='all')

df.dropna(axis=0, thresh=1)



df.dropna(thresh=5)

df.fillna(0)


df["preTestScore"].mean()


df["postTestScore"].median()

df["postTestScore"].mode()

df["preTestScore"].fillna(df["preTestScore"].mean(), inplace=True)


df.groupby("sex")["postTestScore"].transform("mean")

df["postTestScore"].fillna(
    df.groupby("sex")["postTestScore"].transform("mean"), inplace=True)

df[df['age'].notnull() & df['sex'].notnull()]