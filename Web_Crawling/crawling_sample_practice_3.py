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
Chrome_Driver.set_window_size(1120,696)
Chrome_Driver.get("https://korean.visitkorea.or.kr/main/main.do")

time.sleep(2)

Chrome_Driver.find_element(By.XPATH , '//span[@class="input"]/a[@class="btn_search"]').click()
Search = Chrome_Driver.find_element(by = 'id' , value = 'inp_search_index')
Search.send_keys(word)
Search.send_keys('\n')
time.sleep(2)

Chrome_Driver.find_element(By.XPATH,  '//a[@title="여행정보 페이지로 이동"]').click()
time.sleep(2)


name_data_list = []
explain_data_list = []

start_time = time.time()

for i in range(12):
    if i == 3 or i == 7 :
        continue

    xpath = f'//div[@id="search_result"]/ul/li[{i+1}]/a[@class="img"]'
    Chrome_Driver.find_element(By.XPATH , xpath).click()
    time.sleep(2) #시간 설정을 해놓지 않으면 데이터 로드가 되지 않은채로 html 코드를 받기 때문에 name_data의 값이 []이 나온다.

    data = Chrome_Driver.page_source
    full_html_data = BeautifulSoup(data, "html.parser")
    name_data = full_html_data.select('div.titleType1 > h2#topTitle')
    explain_data = full_html_data.select('div.inr_wrap > div.inr > p') #select 함수는 CSS_Selector만 지원하기때문에 Xpath를 사용할 수 없다.
    
    name_data_list.extend(name_data)
    explain_data_list.extend(explain_data)

    Chrome_Driver.back()
    time.sleep(2)


num_list = []
total_name_list = []
total_explain_list = []

for i in range(len(name_data_list)):
    num_list.append(i+1)
    total_name_list.append(name_data_list[i].get_text())
    total_explain_list.append(explain_data_list[i].get_text())

#print(total_name_list)



# 수집한 데이터들을 파일에 저장

place_list = pd.DataFrame()
place_list['번호'] = num_list
place_list['관광명소 이름'] = total_name_list
place_list['설명'] = total_explain_list

xlsx_name = "C:\Data_Analysis_Study\Web_Crawling\\tour.xlsx"

place_list.to_excel(xlsx_name)

end_time = time.time()
print(f"데이터 처리 시간 : {end_time - start_time:.2f}초")

