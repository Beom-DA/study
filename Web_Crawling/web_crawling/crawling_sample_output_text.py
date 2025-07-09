# 추출한 데이터 중 텍스트 데이터만 저장하기
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import time

keyword = input("크롤링할 키워드는 무엇입니까? : ")

upload_path = "C:\Data_Analysis_Study\Web_Crawling\data_test.txt"
orig_stdout = sys.stdout
file = open(upload_path, 'a' , encoding='utf-8')
sys.stdout = file
time.sleep(1)


Chrome_Driver = webdriver.Chrome() # ChromeDriver를 실행
Chrome_Driver.get("https://web.joongna.com/") # 크롬드라이버가 해당 주소로 크롬을 연다
time.sleep(2)

Search = Chrome_Driver.find_element(by = "id", value = "search-box") 
Search.send_keys(keyword)
Search.send_keys("\n")
time.sleep(2)
data = Chrome_Driver.page_source
full_html_data = BeautifulSoup(data,"html.parser")

content_list = full_html_data.select('h2.md\\:text-base')

#print(content_list)

for i in content_list:
    print(i.text.strip())
    print("\n")

sys.stdout = orig_stdout
file.close()
print("끝")





