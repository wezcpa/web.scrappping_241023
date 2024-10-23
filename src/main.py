# 1. 웹페이지 요청
url = 'https://naver.com'
response = requests.get(url)
print(response.status_code)

if respose.status_code == 200:
    print('요청이 성공적입니다.')

