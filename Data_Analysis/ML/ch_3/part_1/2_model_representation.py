import numpy as np # Numpy 라이브러리 호출
weight_vector = np.array([[1], [1], [1]]) # Weight Vector 
x_vector = np.array([[3], [4], [5]])
weight_vector.T.dot(x_vector) # 1 * 3 + 1 * 4 + 1 * 5 = 12

import pandas as pd
data_url = './housing.data' #Data URL
df_data = pd.read_csv(data_url, sep='\s+', header = None) #csv 타입 데이터 로드, separate는 빈공간으로 지정하고, Column은 없음
df_data.columns = ['CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO' ,'B', 'LSTAT', 'MEDV'] 
df_data.head()


df_data['weight_0'] = 1 # weight 0 값 추가
df_data= df_data.drop("MEDV", axis=1) #Y값 제거
df_data.head()

df_matrix = df_data.as_matrix() # Matrix Data로 변환하기
weight_vector =  np.random.random_sample((14, 1))
df_matrix.dot(weight_vector)