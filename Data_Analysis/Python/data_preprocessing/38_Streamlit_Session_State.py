import streamlit as st
import pandas as pd

### 사용자와 interaction 시 변화하는 데이터 유지하기
# st.header('Session State example')

# if 'i' not in st.session_state:
#     st.session_state['i'] = 0

# plus_one = st.button(
#     label= '+1',
#     key='btn_plus1'
# )

# if plus_one :
#     st.session_state['i'] += 1

# st.text('i = {}'.format(st.session_state['i']))


### 캐싱
@st.cache_data
def expensive_computation(a,b):
    st.text('Result : {}'.format(a+b))

result = st.button(
    'Calculate',
    on_click=expensive_computation, args=(3,4)
)