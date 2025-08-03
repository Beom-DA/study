import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform
import plotly.graph_objects as go
from scipy.stats import norm
from scipy.stats import probplot
from scipy.stats import stats
from scipy.stats import boxcox
from just_do_it_정규성_변환 import df

### Z-Score Scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df['log_금액'].values.reshape(-1,1)) # standardscaler는 2차원 배열 입력을 기대하는데 Series는 1차원이라서 에러가 난다.
scaled_series = pd.Series(scaled_data.flatten(), index=df['log_금액'].index)
print('Z-score Scaling mean_value : {:.2f}'.format(scaled_series.mean()))
print('Z-score Scaling std_value : {:.2f}'.format(scaled_series.std()))



### Robust Scaling
from sklearn.preprocessing import RobustScaler

r_scaler = RobustScaler()
r_scaled_data = r_scaler.fit_transform(df['log_금액'].values.reshape(-1,1))
r_scaled_series = pd.Series(r_scaled_data.flatten(), index=df['log_금액'].index)
df['r_scaled_금액'] = r_scaled_series
print('Robust Scaling median_value : {:.2f}'.format(r_scaled_series.median()))

fig, ax = plt.subplots(1,2)
sns.boxenplot(
    data=df, y='log_금액', ax=ax[0]
)
sns.boxenplot(
    data=df, y='r_scaled_금액', ax=ax[1]
)
ax[0].set_title('log transformation')
ax[1].set_title('Robust Scaling Graph')
plt.show()
