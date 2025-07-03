# 추출한 데이터 중 텍스트 데이터만 저장하기

from bs4 import BeautifulSoup
from selenium import webdriver
import time

keyword = input("크롤링할 키워드는 무엇입니까? : ")
#file_name = input("결과를 저장할 파일경로와 이름을 지정하세요")

Chrome_Driver = webdriver.Chrome() # ChromeDriver를 실행
Chrome_Driver.get("https://www.jobkorea.co.kr/") # 크롬드라이버가 해당 주소로 크롬을 연다
time.sleep(2)

Search = Chrome_Driver.find_element(by = "id", value = "AKCFrm") 
Search.send_keys(keyword)
Search.send_keys("\n")

time.sleep(1)

data = Chrome_Driver.page_source
full_html_data = BeautifulSoup(data,"html.parser")

content_list = full_html_data.find("span","Typography_variant_size14__344nw27 Typography_weight_regular__344nw2d Typography_color_gray800__344nw2l")

for i in content_list:
    print(i)
    print("\n")