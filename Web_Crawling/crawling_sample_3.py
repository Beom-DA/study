# find_all() 객체 + .string

from bs4 import BeautifulSoup

with open('HTML_sample_3.html','r', encoding='utf-8') as f:
    ex3 = f.read()
 
soup = BeautifulSoup(ex3 , 'html.parser')


list = soup.find_all('p')
print("p 태그에 해당하는 코드 : ", list)
print("")
print("find_all()객체를 이용한 방법 : ")
for i in list :
    print(i.string)

print("get_text()를 이용한 방법 : ")
for i in list:
    print(i.get_text())
