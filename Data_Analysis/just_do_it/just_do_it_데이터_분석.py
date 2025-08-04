from just_do_it_표준화 import df
# 금액 : df['r_scaled_금액']
# 기온 : df['r_scaled_기온']
# 강수량 : df['r_scaled_강수량']
# 습도 : df['scaled_습도']
# 풍속 : df['scaled_풍속']

import plotly.express as px



############# 기온과 소비액 scatterplot #############
fig = px.scatter(
    data_frame=df, x='r_scaled_기온', y='r_scaled_금액',
    width= 700, height=600
)
fig.update_layout(
    xaxis_title='기온',
    yaxis_title='카드 소비액',
    title = '기온과 카드 소비액의 관계'
)
fig.show()



