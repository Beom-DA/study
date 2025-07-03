#find() 객체

from bs4 import BeautifulSoup

with open('HTML_sample.html','r', encoding='utf-8') as f:
    ex1 = f.read()
 
soup = BeautifulSoup(ex1 , 'html.parser')

print("title 태그에 해당하는 코드 : ", soup.find('title'))
print("")
print("p 태그에 해당하는 코드 : ", soup.find('p'))