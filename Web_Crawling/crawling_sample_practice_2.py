# crawling_sample_output_text.py 에서 했던 예제를 이용해서
# 추가적인 기능을 더 써볼 것이다.
# 첫 번째, DataFrame() 을 써서 데이터를 다루고 저장한다.
# 두 번째, 2 페이지 이상의 데이터 처리 방법을 연습한다.<<<
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import xlwt
from selenium.webdriver.common.by import By

keyword = input("크롤링할 키워드는 무엇입니까? : ")

Chrome_Driver = webdriver.Chrome() # ChromeDriver를 실행
Chrome_Driver.get("https://web.joongna.com/") # 크롬드라이버가 해당 주소로 크롬을 연다
time.sleep(2)

Search = Chrome_Driver.find_element(by = "id", value = "search-box") 
Search.send_keys(keyword)
Search.send_keys("\n")
time.sleep(2)




total_name_data = []
total_price_data = []


for i in range(10): # 10페이지까지의 데이터를 수집
    data = Chrome_Driver.page_source
    full_html_data = BeautifulSoup(data,"html.parser")

    name_data = full_html_data.select('h2.md\\:text-base')
    total_name_data.extend(name_data)
    price_data = full_html_data.select('div.lg\\:mt-1\\.5')
    total_price_data.extend(price_data)

    Chrome_Driver.find_element(by = By.CSS_SELECTOR , value = '.items-center.h-full.flex').click()


num = 1
num_list = []
name_list = []
price_list = []

for i in range(len(total_name_data)):
    num_list.append(num)

    name_list.append(total_name_data[i].get_text())#extend()와 += 중에 extend()가 훨씬 효율적이고 빠르다.

    price_list.append(total_price_data[i].get_text())

    num += 1

laptop_list = pd.DataFrame()
laptop_list['번호'] = num_list
laptop_list['노트북 이름'] = name_list
laptop_list['가격'] = price_list

xlsx_name = "C:\Data_Analysis_Study\Web_Crawling\data_test.xlsx"

laptop_list.to_excel(xlsx_name)