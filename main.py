import func
import face
import nvapi
# func.face('이미지 주소')
news=nvapi.news('불금')
print(news) #nvapi.news에서 전달된 데이터를 출력

# face.py 안에있는 함수 호출
# face.face_func('https://image.ajunews.com/content/image/2015/04/17/20150417162930963180.jpg')