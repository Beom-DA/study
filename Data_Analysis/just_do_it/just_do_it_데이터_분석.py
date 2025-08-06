from just_do_it_표준화 import df
# 금액 : df['r_scaled_금액']
# 기온 : df['r_scaled_기온']
# 강수량 : df['r_scaled_강수량']
# 습도 : df['scaled_습도']
# 풍속 : df['scaled_풍속']

import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


############# 기온과 소비액 scatterplot #############
# corr, _ = pearsonr(df['r_scaled_기온'], df['r_scaled_금액'])
# corr_str = f'correlation : {corr:.2f}'

# fig = px.scatter(
#     data_frame=df, x='r_scaled_기온', y='r_scaled_금액',
#     width= 700, height=600, trendline='ols'
# )
# fig.update_layout(
#     xaxis_title='기온',
#     yaxis_title='카드 소비액',
#     title = '기온과 카드 소비액의 관계'
# )
# fig.add_annotation(
#     xref='paper', yref='paper',
#     x=0.95, y=1,
#     text=corr_str,
#     showarrow=False

# )
# fig.show()



############# 강수량과 소비액 scatterplot #############
# corr, _ = pearsonr(df['r_scaled_강수량'], df['r_scaled_금액'])
# corr_str = f'correlation : {corr:.2f}'

# fig = px.scatter(
#     data_frame=df, x='r_scaled_강수량', y='r_scaled_금액',
#     width= 700, height=600, trendline='lowess'
# )

# fig.update_layout(
#     xaxis_title = '강수량',
#     yaxis_title = '카드 소비량',
#     title='강수량과 카드 소비량의 Scatterplot'
# )
# fig.add_annotation(
#     xref='paper', yref='paper',
#     x=0.95, y=1,
#     text=corr_str,
#     showarrow=False

# )
# fig.show()



############# 습도와 소비액 scatterplot #############

# corr, _ = pearsonr(df['scaled_습도'], df['r_scaled_금액'])
# corr_str = f'correlation : {corr:.2f}'

# fig = px.scatter(
#     data_frame=df, x='scaled_습도', y='r_scaled_금액',
#     width=700, height=600, trendline='ols',
# )
# fig.update_layout(
#     xaxis_title = '습도',
#     yaxis_title = '금액',
#     title = '습도와 금액 ScatterPlot'
# )
# fig.add_annotation(
#     xref='paper', yref='paper',
#     x=0.95, y=1,
#     text=corr_str,
#     showarrow=False

# )
# fig.show()


############# 풍속과 소비액 scatterplot #############
# corr, _ = pearsonr(df['scaled_풍속'], df['r_scaled_금액'])
# corr_str = f'correlation : {corr:.2f}'

# fig = px.scatter(
#     data_frame=df, x='scaled_풍속', y='r_scaled_금액',
#     width=700, height=600, trendline='lowess'
# )
# fig.update_layout(
#     xaxis_title='풍속',
#     yaxis_title='금액',
#     title = '풍속과 카드 소비량 ScatterPlot'
# )
# fig.add_annotation(
#     xref='paper', yref='paper',
#     x=0.9, y=1,
#     text=corr_str,
#     showarrow=False
# )
# fig.show()



################ 독립변수끼리의 다중공신성 확인 #################

X = df[['r_scaled_기온', 'r_scaled_강수량', 'scaled_습도', 'scaled_풍속']]

# 상관계수 행렬 계산 (피어슨 상관계수 기본)
# corr_matrix = X.corr()

# fig, ax = plt.subplots()
# sns.heatmap(
#     data=corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1
# )
# plt.title('독립변수 상관관계 매트릭스')
# plt.show()

### VIF 확인
# from statsmodels.stats.outliers_influence import variance_inflation_factor
# from statsmodels.tools.tools import add_constant

# X = add_constant(X)

# vif_data = pd.DataFrame()
# vif_data["변수"] = X.columns
# vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# print(vif_data)




############## 날씨와 카드 소비량에 대한 다항 회귀 ###############
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

x = df[['r_scaled_기온','r_scaled_강수량','scaled_습도','scaled_풍속']]
y = df['r_scaled_금액']

poly2 = PolynomialFeatures(degree=2, include_bias=False)
x_poly2 = poly2.fit_transform(x)
model2 = LinearRegression().fit(x_poly2, y)

feature_names = poly2.get_feature_names_out(x.columns)

coefficients = model2.coef_   # --> 회귀계수
intercept = model2.intercept_

coef_df = pd.DataFrame({
    '항목' : feature_names,
    '회귀계수' : coefficients
})

coef_df = coef_df.sort_values(by='회귀계수', ascending=False)
print(coef_df)

y_pred2 = model2.predict(x_poly2)
r2 = r2_score(y,y_pred2)
print('r^2 score : ', r2)