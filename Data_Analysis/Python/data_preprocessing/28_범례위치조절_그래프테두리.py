import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl

### 범례 위치 조절하기(Matplotlib & Seaborn)

df = pd.read_csv(r'data_analysis_adv/datasets/CO2_emissions/CO2_emissions.csv')
'''#df['Vehicle Class'].nunique()
fix, ax = plt.subplots()
sns.scatterplot(
    data=df, x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)',
    hue='Vehicle Class', palette='bright',ax=ax
)
ax.legend(bbox_to_anchor=(1.01,1.05))
plt.show()'''
 


### 범례 위치 조절하기(plotly)
fig = px.scatter(
    data_frame=df, x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)', color='Vehicle Class',
    width=700, height=500
)
fig.update_layout(legend_x = 1.2, legend_y = 1)
fig.show()