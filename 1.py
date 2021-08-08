from flask import Flask, render_template



# 1) 플라스크 객체 생성
app = Flask(__name__)

#2) 주소창에 입력할 URL 경로 생성
@app.route('/')
def index():
    return render_template('index.html')






# localhost:http://127.0.0.1:5000/user/Hahyeon
@app.route('/user/<name>')
def user(name):
    favorite = ['pizza', 'chicken', 'ramen']
    test = "this is <h1>Bold</h1>"
    return render_template('user.html', name=name, test=test,favorite=favorite)


# 유효하지 않은 페이지 정의
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500