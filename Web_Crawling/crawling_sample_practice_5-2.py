# 파일 다운로드 크롤러
# Excel이나 CSV 형태의 파일을 다운받는다.


from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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

#f_choice = input(''' 1.xlsx 형식으로 저장하기      2.csv 형식으로 저장하기  
#위 번호 중 저장할 파일 형식의 번호를 선택하세요:  ''')


#웹 브라우저 실행
start_time = time.time()

options = webdriver.ChromeOptions()
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
command_result = Chrome_Driver.execute("send_command", params)

Chrome_Driver.get(url_addr)
Chrome_Driver.maximize_window()
time.sleep(2)

# WebDriverWait에서 element_to_be_clickable() 을 이용해서 원하는 버튼 누르기
# 전체 / KOSPI / KOSDAQ / KONEx 라디오 버튼 선택 후 조회 버튼 누르기
if choice == '1':
    #WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='mktld_0_0']"))).click()
    Chrome_Driver.find_element(By.ID , 'jsSearchButton').click()
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


'''# 다운로드 이미지를 누른다
WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MDCSTAT022_FORM"]/div[2]/div/p[2]/button[2]/img'))).click()

# xlsx, csv를 고른다
if f_choice == '1' :
    WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-type="excel"]/a'))).click()                                   
elif f_choice == '2' :
    WebDriverWait(Chrome_Driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-type="csv"]/a'))).click()'''


import requests
import json
import pandas as pd


def getStockList():

    requestUrl = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'data.krx.co.kr',
        'Origin': 'http://data.krx.co.kr',
        'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020301',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    params = {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT02201',
        'locale' : 'ko_KR',
        'mktld' : 'ATK',
        'strtDd' : '20250630',
        'endDd' : '20250707',
        'share' : '2',
        'money' : '3',
        'csvxls_isNo' : 'False',   
    }


    response = requests.post(requestUrl, params, headers=headers)
    
    
    '''#Byte정보 --> decode --> jason --> dataframe
    dataByte = response.content
    dataDecoded = dataByte.decode('utf8')
    print("dataDecoded = ",dataDecoded)
    data = json.loads(dataDecoded)
    dataJson = json.dumps(data, indent=4)
    df = pd.read_json(dataJson)
    print(df)
    df = df['output']
    #print(type(df[0]), df[0])
    
    newDf = pd.DataFrame(data=[df[0]])

    for i in range(1, df.size):
        newDf = pd.concat([newDf, pd.DataFrame(data=[df[i]])], ignore_index=True)'''
    
    df = pd.DataFrame(response.json()['output'])
    print(df)
    return df


#리스트 정보 받아와서
stocksDf = getStockList()

'''time.sleep(5)


#저장
stocksDf.to_csv('C:\\Data_Analysis_Study\\Web_Crawling\\xlsx_csv\\KRX_data.csv')'''

'''end_time = time.time()
total_time = end_time - start_time
print("소요시간 : ", total_time)
'''

#### 이러한 과정의 흔적이 없이 OTP를 바로 두번째 URL에 제출하면 서버는 이를 로봇으로 인식해 데이터를 주지 않습니다.