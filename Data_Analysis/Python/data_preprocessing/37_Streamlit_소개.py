import pandas as pd
import streamlit as st

### 제목을 생성하는 함수들
# st.title('This is title')
# st.header('This is header')
# st.subheader('This is subheader')

### Streamlit 마크다운, 텍스트, 코드
# st.markdown(
#     '''
#     This is main text.
#     This is how to change the color of 
#     text :red[Red,] :blue[Blue,] :green[Green.]
#     This is **Bold** and *Italic* text
#     '''
# )

# st.text(
#     '''
#     This is main text.
#     This is how to change the color of 
#     text :red[Red,] :blue[Blue,] :green[Green.]
#     This is **Bold** and *Italic* text
#     '''
# )

# code = '''
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.express as px
# import matplotlib as mpl
# import matplotlib.transforms as transforms

# df = sns.load_dataset('diamonds')
# pivot = df.pivot_table(index='color', columns='clarity',
#                     values='price')
# clarity_order = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

# fig = px.imshow(
#     pivot[clarity_order], width=500, height=400, text_auto='4d'
# )

# fig.update_coloraxes(
#     showscale=True,
#     colorscale=[
#         (0, '#ffffff'), (0.5, '#ffffff'), (1, '#0000ff')
#     ]
# )
# fig.show()
# '''

# st.code(code, language='python')



# ### 페이지를 나누는 divide 함수
# st.title('Title 1')
# st.text('Text body 1')

# st.divider()

# st.title('Title 2')
# st.text('Text body 2')


### Streamlit button 함수
# 방법 1
# def button_write():
#     st.write('button activated')

# st.button('Reset', type='primary')
# st.button('activate', on_click=button_write)

# 방법 2
# if st.button('activate'):
#     st.write('button_activated')


### Streamlit checkbox 함수
# 방법 1
# active = st.checkbox('I agree')
# if active :
#     st.text('Great!')
# --> 체크 박스에 체크를 했다 안했다 해보면 text가 나왔다 사라지는걸 볼 수 있다

# 방법 2
# def checkbox_write():
#     st.write('Great!')

# st.checkbox('I agree', on_change=checkbox_write)
# --> 체크 박스에 체크를 했다 안했다 해보면 text가 나왔다가 사라지지 않는 걸 볼 수 있다.

### Streamlit toggle 함수
# toggle = st.toggle(
#     'Turn on the switch!', value = False
# )
# if toggle:
#     st.text('Switch is turned on!')
# else:
#     st.text('Switch is turned off!')


### Streamlit selectbox 함수
# 방법 1
# option = st.selectbox(
#     label='your selection is',
#     options=['Car', 'Airplane', 'Train', 'Ship']
# )
# st.text('you selected : {}'.format(option))

# 방법 2
# option = st.selectbox(
#     label='your selection is',
#     options=['Car', 'Airplane', 'Train', 'Ship'],
#     index=None,
#     placeholder='select transportation'
# )
# st.text('you selected : {}'.format(option))


### Streamlit radio 함수
# option = st.radio(
#     'what is your favorite movie genre',
#     ['Comedy', 'Drama', 'Documentary'],
#     captions=['Laugh out loud', 'Get the popcorn', 'Never stop learning']
# )

# if option:
#     st.text('You selected : {}'.format(option))



### Streamlit multiselect 함수
# option = st.multiselect(
#     label='yout selection is',
#     options=['Car', 'Airplane', 'Train', 'Ship'],
#     placeholder='select transportation'
# )
# st.text('you selected : {}'.format(option))



### Streamlit text_input 함수
# 방법 1 암호화 X
# string = st.text_input(
#     'Movie title',
#     placeholder='write down the title of your favorite movie'
# )
# if string:
#     st.text('Your answer is ' + string)

# 방법 2 암호화 O
# string = st.text_input(
#     'Movie title',
#     placeholder='write down the title of your favorite movie',
#     type='password'
# )
# if string:
#     st.text('Your answer is ' + string)


### Streamlig file_uploader 함수
# file = st.file_uploader(
#     'Choose a filr' , type='csv', accept_multiple_files=False
# )
# if file is not None:
#     df = pd.read_csv(file)
#     st.write(df.head(5))


### Streamlit slider 함수
# score = st.slider('Your score is...', 0, 100, 1)
# st.text('Score : {}'.format(score))

# from datetime import time

# start_time, end_time = st.slider(
#     'Working time is ...',
#     min_value = time(0), max_value = time(23),
#     value = (time(8), time(18)),
#     format='HH:mm'
# )
# st.text('Working time : {}, {}'.format(start_time, end_time))


### Matplotlib & Seaborn을 통해 그린 그래프 표현
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = sns.load_dataset('tips')
# fig, ax = plt.subplots()
# sns.histplot(
#     data=df, x='total_bill', ax=ax, hue='time'
# )
# st.pyplot(fig)

### Plotly 통해 그린 그래프 표현
# import plotly.express as px

# fig2 = px.box(
#     data_frame=df, x='day', y='tip',
#     facet_col='smoker', facet_row='sex',
#     width=800, height=800
# )
# st.plotly_chart(fig2)


### (활용) Streamlit 앱에서 원하는 변수를 선택하여 그래프 그리기
# import plotly.express as px
# import seaborn as sns

# df = sns.load_dataset('tips')

# x_options = ['day', 'size']
# y_options = ['total_bill', 'tip']
# hue_options = ['smoker', 'sex']

# x_options = st.selectbox(
#     'Select X-axis',
#     index=None,
#     options=x_options
# )
# y_options = st.selectbox(
#     'Select Y-axis',
#     index=None,
#     options=y_options
# )
# hue_options = st.selectbox(
#     'Select Hue-axis',
#     index=None,
#     options=hue_options
# )

# if (x_options != None) & (y_options != None):
#     if hue_options != None:
#         fig3 = px.box(
#             data_frame=df, x=x_options, y=y_options,
#             color=hue_options, width=500
#         )
#     else:
#         fig3 = px.box(
#             data_frame=df, x=x_options, y=y_options,
#             width=500
#         )

# st.plotly_chart(fig3)


### Streamlit 앱에 이미지 생성하기
# from PIL import Image

# img = Image.open(r'data_analysis_adv/datasets/images/image1.jpg')
# st.image(img, width=500, caption='Image from Unsplash')


### 사이드바 생성하기
# st.title('This is main page')

# with st.sidebar:
#     st.title('This is sidebar')
#     side_option = st.multiselect(
#         label='your selection is',
#         options=['Car', 'Airplane', 'Train', 'Ship'],
#         placeholder='select transportation'
#     )


### column 생성하기
# from PIL import Image
# img2 = Image.open(r'data_analysis_adv/datasets/images/image2.jpg')
# img3 = Image.open(r'data_analysis_adv/datasets/images/image3.jpg')

# col1, col2 = st.columns(2)

# with col1 :
#     st.header('Lemonade')
#     st.image(img2, width=300, caption='Image from Unsplash')

# with col2 :
#     st.header('Cocktail')
#     st.image(img3, width=300, caption='Image from Unsplash')


### tab 생성하기
# import plotly.express as px

# tab1, tab2 = st.tabs(['Table', 'Graph'])

# df = pd.read_csv(r'data_analysis_adv/datasets/medical_cost/medical_cost.csv')
# df = df.query('region == "northwest"')

# with tab1 :
#     st.table(df.head(5))

# with tab2 : 
#     fig = px.scatter(
#         data_frame=df, x='bmi', y='charges'
#     )
#     st.plotly_chart(fig)


### expander 생성하기
df = pd.read_csv(r'data_analysis_adv/datasets/medical_cost/medical_cost.csv')
df = df.query('region == "northwest"')

with st.expander('See data table'):
    st.table(df.head(5))