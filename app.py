from flask import Flask, request ,render_template
import face

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True)