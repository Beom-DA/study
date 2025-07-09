# 이미지 파일 크롤링

from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import urllib
import time
import sys
import math
import os


file_dir = 'C:\Data_Analysis_Study\Web_Crawling\\'
query_txt = '사진 저장'

current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
#y_m_d_h_m_s = '%04d-%02d-%02d-%02d-%02d-%02d' % (current_time.tm_year, current_time.tm_mon, current_time.tm_mday, current_time.tm_hour, current_time.tm_min, current_time.tm_sec)

#파일을 저장할 폴더 생성
name_of_folder = file_dir + current_time + '-' + query_txt
os.makedirs(name_of_folder)

Chrome_Driver = webdriver.Chrome()
Chrome_Driver.set_window_size(1120, 696)
Chrome_Driver.get('https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=d8db847f-b262-4048-90a4-6aa4b20bee6e&con_type=10100')
time.sleep(2)

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)

scroll_down(Chrome_Driver)

start_time = time.time()

file_number = 0
data = Chrome_Driver.page_source
full_html_data = BeautifulSoup(data, "html.parser")

img_resource = full_html_data.select('div.img_typeBox.typeFix.clfix > div > button > img')
img_list = []
for i in img_resource:
    img = i['src']
    img_list.append(img)

os.chdir(name_of_folder)
for i in range(len(img_list)):
    try:
        urllib.request.urlretrieve(img_list[i], str(file_number) + '.jpg')
        
    except:
        continue

    file_number += 1
    time.sleep(1)

end_time = time.time()

total_time = end_time - start_time
print("총 걸린 시간 : ", total_time)