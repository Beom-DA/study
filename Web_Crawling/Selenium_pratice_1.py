#필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다.
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

query_txt = input("크롤링할 키워드는 무엇입니까? : ")

#path = "C:\chromedriver.exe" -- > selenium이 업데이트 돼서 크롬드라이버를 다운받지 않아도 됨
driver = webdriver.Chrome()

driver.get("https://www.naver.com")
time.sleep(2)


#try :
#    driver.find_element_by_xpath('//*[@id="chkForm01"]').click()
#except:
#    print("코로나 창이 없습니다.")


element = driver.find_element(by = 'id',value = "query")
element.send_keys(query_txt)
element.send_keys("\n")
