# matplotlib으로 그래프 그리기

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
tips = tips.rename({'sex' : 'gender'}, axis = 'columns')
#print(tips.head())

# 히스토그램 그래프
'''fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1) #격자 생성(1행 1열 첫 번째)

axes1.hist(tips['total_bill'], bins = 10)
axes1.set_title("Histogram of Total Bill")
axes1.set_xlabel("Total bill")
axes1.set_ylabel("Frequency")
plt.show()'''


# 산점도 그래프
'''scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
plt.show()'''


# 박스 그래프
#print(tips)
'''boxplot = plt.figure()
axes1 = boxplot.add_subplot(1,1,1)

axes1.boxplot([tips[tips['gender'] == 'Female']['tip'], tips[tips['gender'] == 'Male']['tip']],labels = ['Female', 'Male'])

axes1.set_xlabel('Gender')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Gender')
plt.show()'''


# 한글 적용
'''import platform
 
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') '''

# 다변량 그래프
'''def recode_gender(gender):
    if gender == 'Female':
        return 0
    else: 
        return 1
    
tips['gender color'] = tips['gender'].apply(recode_gender)

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1,1,1)
axes1.scatter(
    x = tips['total_bill'],
    y = tips['tip'],
    s = tips['size'] * 10,
    c = tips['gender color'],
    alpha = 0.5 # 투명도
)

axes1.set_title('Total Bill vs Tip Colored by 성별 and Sized by 인원 수')
axes1.set_xlabel('지불 금액')
axes1.set_ylabel('팁')
plt.show()
'''

# Seaborn 라이브러리 이용해서 그래프 그리기
# 단변량 그래프
'''fig, ax = plt.subplots()
sns.histplot(data=tips, x="total_bill", kde=True, ax=ax)
ax.set_title("Total Bill Histogram with Density Plot")
#ax.set_ylabel("Frequency")
plt.show()'''


# 이변량 그래프
'''ax = plt.subplots()
ax = sns.regplot(x = 'total_bill', y = 'tip', data = tips, fit_reg = True)
ax.set_title('ScatterPlot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()'''


# 산점도와 히스토그램을 한 번에 그려주는 jointplot 메소드 사용
'''joint = sns.jointplot(x='total_bill', y='tip', data = tips)
joint.set_axis_labels(xlabel='Total bill', ylabel = 'Tip')
joint.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize = 13, y = 1.03)
plt.show()'''

# 육각 그래프(hexbin)
'''hexbin = sns.jointplot(x='total_bill', y='tip', data = tips, kind = 'hex')
hexbin.set_axis_labels(xlabel='Total bill', ylabel = 'Tip')
hexbin.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize = 13, y = 1.03)
plt.show()'''

# 이차원 밀집도 그리기
ex = plt.subplots()
ex = sns.kdeplot(x = tips['total_bill'],
                 y = tips['tip'],
                 shade = True)
ex.set_title('Kernel Density Plot of Total Bill and Tip')
ex.set_xlabel('Total Bill')
ex.set_ylabel('Tip')
plt.show()