import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform

df = pd.read_csv(r'Data/통합데이터.csv')
df['날짜'] = pd.to_datetime(df['날짜'], format='%Y-%m-%d')

category_col = ['물품분류', '시간', '성별', '나이', '요일']
df_encoded = pd.get_dummies(df, columns=category_col, drop_first=True)
print(df_encoded.head())