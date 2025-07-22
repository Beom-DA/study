import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl

### 그래프 내 텍스트 표현(Matplotlib & Seaborn)
'''df = pd.read_csv(r'data_analysis_adv/datasets/CO2_emissions/CO2_emissions.csv')

fig, ax = plt.subplots()
sns.scatterplot(
    data=df, x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)', ax=ax, hue='Fuel Type'
)
# ax.text(
#     x=10, y=130,
#     s='fuel type ethanol emits less CO2',
#     fontdict={'fontsize': 12, 'weight' : 'bold'}
# )

# ax.text(
#     x=0.3, y=.12,
#     s='fuel type ethanol emits less CO2',
#     fontdict={'fontsize': 12, 'weight' : 'bold'},
#     transform = ax.transAxes
# )

ax.annotate(
    text='ethanol is efficient', xy=(0.95, 0.7),
    xytext=(0.73, 0.5), arrowprops={'color' : 'black', 'width' : 1},
    xycoords=ax.transAxes
)

plt.show()'''



### 그래프 내 텍스트 표현(Plotly)
df = pd.read_csv(r'data_analysis_adv/datasets/CO2_emissions/CO2_emissions.csv')

fig = px.scatter(
    data_frame= df, x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)', width=700, height=400,
    color='Fuel Type'
)

fig.add_annotation(
    x=20, y=130, text='<b>fuel type ethanol emits less CO2</b>',
    showarrow=False
)

fig.add_annotation(
    x=0.9, xref='x domain', y=0.75, yref='y domain',
    text='ethanol is efficient',
    showarrow=True, arrowhead=5
)
fig.show()