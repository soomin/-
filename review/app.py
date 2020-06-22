from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분/css/js 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    # 전달받은 데이터를 꺼내고
    # 그 데이터를 디비에 저장
    # 잘 됐다고 알려주기
    # 파이썬은 세미콜론 안붙힘
    print(request.form)
    title = request.form['title_give']
    author = request.form['author_give']
    review = request.form['review_give']

    doc={
        'title':title,
        'author':author,
        'review':review
    }

    db.reviews.insert_one(doc)

    return jsonify({'result':'success', 'msg': '저장됨'})
    # 이게 html에서success(response)의 response.


@app.route('/reviews', methods=['GET'])
def read_reviews():
    # 적힌 리뷰들 불러와서
    reviews=list(db.reviews.find({},{'_id':0}))
    # db.reviews.find({'찾을조건'},{'필요없는 조건'})
    # 크롬에게 돌려주기

    return jsonify({'result':'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)