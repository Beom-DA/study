import pandas as pd
import streamlit as st
import plotly.express as px



def load_dataset(path):
    return pd.read_csv(path)

path = r'data_analysis_adv/datasets/CO2_emissions/CO2_emissions.csv'
df = load_dataset(path)
# print(df.head().T)

### 사이드바 생성 및 필터 설정
makers = df['Vehicle Class'].unique().tolist()

with st.sidebar:
    st.markdown('Filter the data you want to analyze : :tulip:')

    st.multiselect(
        'Select the vehicle class you want to analyze',
        options=makers, default=['TWO-SEATER'],
        key='maker_filter'            
    )

    st.slider(
        'Select the engine size (Liter) you want to analyze: ',
        min_value= df['Engine Size(L)'].min(),
        max_value= df['Engine Size(L)'].max(),
        value=(df['Engine Size(L)'].quantile(0.1), df['Engine Size(L)'].quantile(0.95)),
        step=3.0,# 슬라이더를 조작할 때 값이 증가하는 간격
        key='engine_filter'
        # min_value, max_value, step과 같은 수치 변수들의 타입이 동일해야한다.(여기선 float)
    )

df = df.loc[
    (df['Vehicle Class'].isin(st.session_state['maker_filter'])) &
    (df['Engine Size(L)'] < st.session_state['engine_filter'][1]) &
    (df['Engine Size(L)'] > st.session_state['engine_filter'][0]) 
]

# st.header('차량 세부사항')
# df


### 메인 페이지 구성
st.title('Data Analysis - CO2 Emission')

st.write(
    '''
    이 웹페이지는 ~~대한 데이터 분석 페이지입니다.
    '''
)
st.divider()

### 그래프 1
st.subheader(
    'Analysis of Engine Size'
)

col1, col2 = st.columns(2)
with col1:
    st.write(
        '''
        box plot of engine sizes by automotive manufacturer. ~~
        '''
    )

with col2:
    fig1 = px.box(
        data_frame=df.sort_values('Engine Size(L)', ascending=False),
        x='Make', y='Engine Size(L)', width=500, height=400, points='all' # points
    )
    st.plotly_chart(fig1)

st.divider()

### 그래프 2
st.subheader('Analysis of Fuel Consumption')

col3, col4 = st.columns(2)
with col3:
    st.write(
        '''
        The scatter plot~~~~~
        '''
    )
    st.selectbox(
        'Select Y-axis',
        [
            'Fuel Consumption City (L/100 km)',
            'Fuel Consumption Hwy (L/100 km)',
            'Fuel Consumption Comb (L/100 km)'
        ],
        key='fig2_yaxis'
    )

with col4:
    fig2=px.scatter(
        data_frame=df, x='Engine Size(L)', y=st.session_state['fig2_yaxis'],
        width=500, color='Make', trendline='ols', trendline_scope='overall'
    )
    st.plotly_chart(fig2)

st.divider()

### 그래프 3
st.subheader('Analysis of Carbon Emissions')

col5, col6 = st.columns(2)
with col5:
    st.write(
        '''
        The scatter plot graph depicting the correlation between fuel ~~~
        '''
        # '''는 여러줄 문법이다.
    )
    st.selectbox(
        'Select X-axis',
        [
            'Fuel Consumption City (L/100 km)',
            'Fuel Consumption Hwy (L/100 km)',
            'Fuel Consumption Comb (L/100 km)'
        ],
        key='fig3_xaxis'
    )

with col6:
    fig3 = px.scatter(
        data_frame=df, x=st.session_state['fig3_xaxis'], y='CO2 Emissions(g/km)',
        width=500, color='Make', trendline='ols', trendline_scope='overall'
    )
    st.plotly_chart(fig3)

st.divider()