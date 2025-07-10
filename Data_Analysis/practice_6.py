# Pandas 자료형

import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")
#print(tips)

tips = tips.rename({'sex' : 'gender'}, axis = 'columns') 
#print(tips)

# 여러 자료형을 문자열로 변환하기
tips['gender_str'] = tips['gender'].astype(str)
tips['total_bill'] = tips['total_bill'].astype(str)
#print(tips.dtypes)

# 잘못입력한 데이터 처리
# 정수형으로 변환하는 to_numeric 메소드
tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1,3,5,7], 'total_bill'] = 'missing'
# --> total_bill 의 자료형이 이로써 object로 바꼈다.
# errors 인자에 설정할 수 있는 값
# — raise : 숫자롤 변환할 수 없는 값이 있으면 오류 발생(기본값)
# — coerce : 숫자로 변환할 수 없는 값을 누락값(NaN)으로 지정
# — ignore : 아무 작업도 하지 않음
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors = 'coerce')
'''print(tips_sub_miss.dtypes)
print(tips_sub_miss)'''


# 다운캐스팅
tips_sub_miss['total_bill'] = pd.to_numeric( tips_sub_miss['total_bill'], errors='coerce', downcast='float')
 
#print(tips_sub_miss.dtypes)


# Category 자료형
print(tips.info())
tips['gender'] = tips['gender'].astype(str)
print(tips.info())
tips['gender'] = tips['gender'].astype('category')