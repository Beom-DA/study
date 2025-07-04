# crawling_sample_output_text.py 에서 했던 예제를 이용해서
# 추가적인 기능을 더 써볼 것이다.
# 첫 번째, DataFrame() 을 써서 데이터를 다루고 저장한다.
# 두 번째, 2 페이지 이상의 데이터 처리 방법을 연습한다.
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

keyword = input("크롤링할 키워드는 무엇입니까? : ")



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

laptop = pd.DataFrame()









