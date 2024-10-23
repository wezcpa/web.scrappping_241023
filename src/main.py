# 1. 웹페이지 요청

import requests

url = 'https://naver.com'
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    print('요청이 성공적입니다.')

