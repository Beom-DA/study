#css_selector 이용하여 원하는 데이터 추출

from bs4 import BeautifulSoup

with open('HTML_sample_4.html','r', encoding='utf-8') as f:
    ex4 = f.read()
 
soup = BeautifulSoup(ex4 , 'html.parser')


print("p 태그에 해당하는 코드 : ", soup.select('p'))
print("")
print("class 속성의 값으로 추출한 데이터 : ", soup.select('.name1'))
print("")
print("id 속성 값으로 추출한 데이터 : ", soup.select("#fruits2"))
print("")
print("단계적으로 태그를 나눈 데이터 : ", soup.select('div > p > span'))
