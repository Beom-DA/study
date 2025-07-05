#한국관광공사 홈페이지에 들어가서 
#검색어를 입력하고
#검색한 페이지에서 첫 번째부터 마지막 게시글까지의 정보를 모은다.
#다음 페이지로 넘어가서 다시 게시글들의 정보를 모은다.

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import xlwt
from selenium.webdriver.common.by import By

word = input("검색어를 입력하세요 : ")

Chrome_Driver = webdriver.Chrome()
Chrome_Driver.get("https://korean.visitkorea.or.kr/main/main.do")
time.sleep(2)

Chrome_Driver.find_element(By.XPATH , '//span[@class="input"]/a[@class="btn_search"]').click()
Search = Chrome_Driver.find_element(by = 'id' , value = 'inp_search_index')
Search.send_keys(word)
Search.send_keys('\n')
time.sleep(2)

Chrome_Driver.find_element(By.XPATH,  '//a[@title="여행정보 페이지로 이동"]').click()
time.sleep(2)

data = Chrome_Driver.page_source
full_html_data = BeautifulSoup(data, "html.parser")


i = 1
xpath = f'//div[@id="search_result"]/ul/li[{i}]/a[@class="img"]'
Chrome_Driver.find_element(By.XPATH , xpath).click()
time.sleep(2)
