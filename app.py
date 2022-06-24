from flask import Flask, request ,render_template
import face
import nvapi
from ast import keyword
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/a')
def a():
    return 'Hello,a!'


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        #이미지 URL 받기
        url=request.form["URL"]
        #관상 코드 실행
        face.face_func(url)
        return f'''
                AI가 분석한 결과입니다.
                "<img src='{url}'width='320'height='320'>
                <img src=/static/img/face.png 'width='320'height='320'>"
                '''

@app.route('/newsapi', methods=['GET', 'POST'])
def newsapi():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        #뉴스 검색어 받기
        keyword=request.form["keyword"]
        #네이버 뉴스 정보 받아오는 코드 실행
        news=nvapi.news(keyword)
        return news
        # return f'''
        #         유저가 검색한 내용<mark>{keyword}</mark>의
        #         뉴스 정보가 나와야 한다.
        #         '''

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True)