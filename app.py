from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return '안녕'
    
    '''
    각주인데 뭐넣지
    '''
@app.route('/hello')
def hello():
    return render_template("main.html")

@app.route('/hell')
def hell():
    return '테스트로 돌리는 2서버인데요'

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/action_page', methods=['GET','post'])
def action_page():
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else:
        #여기 POST로 들어오는 데이터를 받아보자
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값:", email, pwd)
        return '회원가입 데이터(post)<br>{}입니다.'

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login_page', methods=['GET','post'])
def login_page():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        #여기 POST로 들어오는 데이터를 받아보자
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값:", email, pwd)
        #만약에 이메일과 패스워드 같다면
        if email == 'a@a.com' and pwd == '1234':
        #로그인 성공
            return '로그인 성공'
        #아니면
        else:
        #아이디 패스워드 확인
            return '아이디 패스워드 확인'
        
        return '로그인 데이터(post)'
    


@app.route('/naver')
def naver():
    return render_template("naver.html")
    
@app.route('/gonaver', methods=['GET', 'POST'])
def gonaver():
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else:
        #여기 POST로 들어오는 데이터를 받아보자

        search = request.form['fname']
        print("전달된값:", search)
        return '당신이 검색한 키워드(post)<br>{}입니다.'
    

if __name__ == '__main__':
    app.run()