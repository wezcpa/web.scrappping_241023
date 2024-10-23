#셀레니엄 설치
#PS C:\Users\Owner\OneDrive\9. Pending\Python_SYS\python 셀레니움> cd .venv
#PS C:\Users\Owner\OneDrive\9. Pending\Python_SYS\python 셀레니움\.venv> cd Scripts
#PS C:\Users\Owner\OneDrive\9. Pending\Python_SYS\python 셀레니움\.venv\Scripts> .\activate
#(.venv) PS C:\Users\Owner\OneDrive\9. Pending\Python_SYS\python 셀레니움\.venv\Scripts> pip install selenium

# 웹페이지 열기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

# 네이버 웹페이지 열기
driver = webdriver.Chrome(options=options)
url = 'https:\\naver.com'
driver.get(url)
time.sleep(3)

# 네이버 웹페이지에서 검색창에 검색어 입력하기
query = driver.find_element(By.ID, 'query')
query.send_keys('인공지능')
# 위 2줄을 한줄로 코딩하면
# driver.find_element(By.ID, 'query').send_keys('인공지능')
time.sleep(2)

# 네이버 웹페이지에서 검색아이콘 클릭하기
serch_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")
serch_btn.click()
time.sleep(2)

# 검색 아이콘 클릭 대신에 "엔터" 클릭해서 이동하기
# driver.find_element(By.ID, 'query').send_keys(Keys.ENTER)

# 스크린샷 저장하고 창닫기
driver.save_screenshot("naver_인공지능.png")
driver.quit()
