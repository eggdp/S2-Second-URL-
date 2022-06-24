# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "Bew9FydKjBcsUDMpmLze"
client_secret = "meYgfItdc5"
encText = urllib.parse.quote("불금")
def news(keyword):
    ret=""
    encText=urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        ret = response_body.decode('utf-8')
    else:
        # print("Error Code:" + rescode)
        ret="Error Code:"+rescode

    return ret #결과 값을 함수밖으로 전달합니다.