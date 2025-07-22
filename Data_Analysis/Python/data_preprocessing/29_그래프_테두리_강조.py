import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl

### 그래프 테두리 강조(Matplotlib & Seaborn)
'''df = pd.read_csv(r'data_analysis_adv/datasets/CO2_emissions/CO2_emissions.csv')

fig, ax = plt.subplots()

sns.boxplot(
    data=df, x='Cylinders', y='CO2 Emissions(g/km)',
    ax=ax
)
spines = ['left', 'right', 'top', 'bottom']
for spine in spines:
    ax.spines[spine].set_color('blue')
    ax.spines[spine].set_linewidth(3)

plt.show()'''

### 그래프 테두리 강조(Plotly)
df = pd.read_csv(r'data_analysis_adv/datasets/CO2_emissions/CO2_emissions.csv')

fig = px.box(
    data_frame=df, x='Cylinders', y='CO2 Emissions(g/km)',
    width = 500, height=500
)
fig.update_xaxes(showline=True, linecolor='black',
                 linewidth=3, mirror=True)
fig.update_yaxes(showline=True, linecolor='black',
                 linewidth=3, mirror=True)

fig.show()