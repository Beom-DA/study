import numpy as np
import pandas as pd




def get_rating_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename).sort_values(['source', 'target'])
    pivot = pd.pivot_table(data=df, index='source', columns='target', values='rating').fillna(0)
    arr = np.array(pivot)
    return arr

# filename = r'movie_rating.csv'
# print(get_rating_matrix(filename))


def get_frequent_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename).sort_values(['source', 'target'])
    df = df.set_index('source')
    df = df.groupby('source')['target'].sum()
    return df

filename = r'1000i.csv'
print(get_frequent_matrix(filename))
