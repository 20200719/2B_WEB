from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return '안녕'
    
    '''
    각주인데 뭐넣지
    '''
@app.route('/hell')
def hell():
    return render_template("main.html")

@app.route('/hello')
def hello():
    return '테스트로 돌리는 2서버인데요'

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