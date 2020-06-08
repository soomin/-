from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
# @app.route('/')는 루트패쓰를 줬을 때 home이라는 함수 값을 준다는 것.
# 슬래시라는 곳에 요청을 날렸을 때 밑에 home 응답값을 준다.
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!','title_receive':title_receive})
   # 요청사항에 타이틀기브라는 데이터를 데이터 보내는 값에 넣어주면 리퀘스트 폼에 받게 된다
# 경로가 겹쳐도 되는데 method가 다를 때만 가능. (post/get)
# 브라우저에 직접 요청하긴 힘들고, ajax를 이용
# ajax로


@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!','title':title_receive})
   # get은 쿼리파라미터는 request.args.get으로 함.
   # args가 쿼리파라미터 데이터가 들어가있는 저장공간
   # title_give라는 키 값을 쿼리파라미터의 값을 가져와야함.
   # print문이 실행되면 내가 크롬에서 localhost:5000/test?title_give?____에서 입력한 ____값 출력
   # test경로로 겟방식 요청하면 아래 함수가 실행 됨. 타이틀기브라는 키 값을 쿼리파라미터에서 찾아서 타이틀 리시브라는 값에 저장을 하고 
   # 변수를 프린트하여 제이슨화한 키값을 반환함.

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)