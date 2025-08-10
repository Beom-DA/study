import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic') # 한글 인코딩
plt.rc('axes', unicode_minus=False) # xlabel, ylabel 음수의 '-' 인코딩

s = pd.Series([-4,0,1,3,5,-2,5]).plot(table=itle='한글폰트 설정')
plt.show()