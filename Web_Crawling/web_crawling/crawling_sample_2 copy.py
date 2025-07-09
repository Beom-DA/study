# find_all() 객체

from bs4 import BeautifulSoup

with open('HTML_sample_2.html','r', encoding='utf-8') as f:
    ex2 = f.read()
 
soup = BeautifulSoup(ex2 , 'html.parser')

print("title 태그에 해당하는 코드 : ", soup.find('title'))
print("")
print("p 태그에 해당하는 코드 : ", soup.find_all('p'))
print("")
print("아무 것도 없는 태그 : ", soup.find('div'))