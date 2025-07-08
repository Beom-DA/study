# 파일 다운로드 크롤러
# Excel이나 CSV 형태의 파일을 다운받는다.


from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import pandas as pd
from io import BytesIO

#url_addr = input("1. 웹 페이지 주소를 입력하세요 : ")
url_addr = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020301'
#f_dir = input("2. 파일이 저장될 경로를 쓰세요 : ")
f_dir = 'C:\\Data_Analysis_Stud\\Web_Crawling\\xlsx_csv'

if os.path.isdir(f_dir): #존재하는 경로인지 확인
    print("경로 확인\n")
else:
    os.makedirs(f_dir)
    print("경로 생성")

choice = input(''' 1.전체      2.KOSPI     3.KOSDAQ   4.KONEX
위 번호 중 조회할 시장 번호를 선택하세요:  ''') #''' ''' 은 여러줄을 띄우고 싶을 때 사용.

f_choice = input(''' 1.xlsx 형식으로 저장하기      2.csv 형식으로 저장하기  
위 번호 중 저장할 파일 형식의 번호를 선택하세요:  ''')


#웹 브라우저 실행
start_time = time.time()

'''options = webdriver.ChromeOptions()
options.add_experimental_option("prefs",{
    "download.default_directory": f_dir, #다운로드 될 파일의 저장폴더 지정
    "download.prompt_for_download": False, # prompt 창이 뜨지 않는다
    "plugins.always_open_pdf_externally": True # pdf형식이 다운로드 되면 브라우저에서 보이지 않고 다운로드된다.
})
Chrome_Driver = webdriver.Chrome(options=options)


#크롬 드라이버는 악의적인 행동을 예방하기 위해 소프트웨어가 컴퓨터에서 파일을 다운로드 하지 못하도록 한다.
#이를 해결하기 위해 크롬 커맨드라인에 다운로드를 허용하는 명령을 추가해야 한다.
Chrome_Driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': f_dir}}
command_result = Chrome_Driver.execute("send_command", params)'''

Chrome_Driver = webdriver.Chrome()
Chrome_Driver.get(url_addr)
Chrome_Driver.maximize_window()
time.sleep(2)

# WebDriverWait에서 element_to_be_clickable() 을 이용해서 원하는 버튼 누르기
# 전체 / KOSPI / KOSDAQ / KONEx 라디오 버튼 선택 후 조회 버튼 누르기
if choice == '1':
    #WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='mktld_0_0']"))).click()
    #Chrome_Driver.find_element(By.ID , 'jsSearchButton').click()
    print("ALL")
elif choice == '2':
    WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='mktId_0_1']"))).click()
    Chrome_Driver.find_element(By.ID , 'jsSearchButton').click()
elif choice == '3':
    WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='mktId_0_2']"))).click()
    Chrome_Driver.find_element(By.ID , 'jsSearchButton').click()
elif choice == '4':
    WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='mktId_0_3']"))).click()
    Chrome_Driver.find_element(By.ID , 'jsSearchButton').click()
else :
    print("번호를 다시 확인해 주세요")


# 다운로드 이미지를 누른다
WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MDCSTAT022_FORM"]/div[2]/div/p[2]/button[2]/img'))).click()

# xlsx, csv를 고른다
if f_choice == '1' :
    WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-type="excel"]/a'))).click()                                   
elif f_choice == '2' :
    WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-type="csv"]/a'))).click()


# generate.cmd를 이용해 otp 코드를 요청한다
gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
gen_otp_STK = {
    'locale' : 'ko_KR',
    'mktld' : 'STK',
    'strtDd' : '20250627',
    'endDd' : '20250704',
    'share' : '2',
    'money' : '3',
    'csvxls_isNo' : 'false',
    'name' : 'fileDown',   
    'url' : 'dbms/MDC/STAT/standard/MDCSTAT02201'
}

headers = {
    'Referer' : 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020301',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

otp_stk = requests.post(gen_otp_url, gen_otp_STK, headers=headers).text # otp 받기

down_url = "http://data.krx.co.kr/comm/fileDn/download_excel/download.cmd"
down_sector_stk = requests.post(down_url, {'code' : otp_stk}, headers=headers) #결과 : <Response [200]>
print("csv 파일 맞음? ", down_sector_stk.headers['Content-type'])
print(down_sector_stk.status_code)
print(down_sector_stk.content[:200])

'''import zipfile
with zipfile.ZipFile(BytesIO(down_sector_stk.content)) as z:
    # 내부 파일 이름 확인
    print(z.namelist())  # ['example.csv'] 이런 식으로 나옴

    # 첫 번째 파일을 읽는다고 가정
    csv_filename = z.namelist()[0]

    with z.open(csv_filename) as f:
        # 인코딩은 다시 cp949나 chardet 등으로 시도
        df = pd.read_excel(f, encoding='euc-kr')  # 또는 'euc-kr', 'utf-8-sig'

print(df.head())'''

df = pd.read_excel(BytesIO(down_sector_stk.content), engine = 'openpyxl')
#print(df.head()) #.head()는 상위 5개의 햄만 출력하는 함수
print(df)
'''sector_stk = pd.read_csv(BytesIO(down_sector_stk.content), encoding = 'UTF-8')
sector_stk.head()
'''
'''scraper = cloudscraper.create_scraper()
response = scraper.post(gen_otp_url, params = gen_otp_STK)
otp = response.text
print("result : ", response)
print("otp : ", otp)

xlsx_url = 'http://data.krx.co.kr/comm/fileDn/download_excel/download.cmd'
xlsx_form_data = scraper.post(xlsx_url, params = {'code':otp})
#xlsx_form_data.encoding = 'EUC-KR'
#xlsx_form_data.text
time.sleep(2)
print(xlsx_form_data.text)'''

end_time = time.time()
total_time = end_time - start_time
print("소요시간 : ", total_time)


