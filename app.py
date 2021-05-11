from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
<html>
<body>

<h1>웹앱프로그래밍</h1>

<p><a href="https://www.w3schools.com/">Visit W3Schools.com!</a></p>
<p><a href="http://localhost:5000/hello">헬로 페이지</a></p>
<p><a href="http://localhost:5000/naver">네이버 페이지</a></p>
</body>
</html>
'''

@app.route('/hello')
def hello():
    return '테스트로 돌리는 2서버인데요'

@app.route('/naver')
def naver():
    return '귀하신 곳에 누추한 네이버가'

if __name__ == '__main__':
    app.run()