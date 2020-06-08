from flask import flask, reder_template, jsonify, request
app=flask(__name__)

from pymongo import MongoClient
client=mongoclient('localhost',27017)
db=client.dbsparta

@app.route('/')
  def home():
    return render_template('index.html')

@app.route('/memo',methods=['post'])
 def write_article():
   url=request.form['url']
   comment=request.form['comment']

   db.article.insert_one({
     "url"=url,
     "comment"=comment
   })

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_image = og_image['content']
    url_title = og_title['content']
    url_description = og_description['content']

    article = {'url': url, 'comment': comment, 'image': url_image,
               'title': url_title, 'desc': url_description}

  db.articles1.insert_one(article)

    return jsonify({'result': 'success'})

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    articles_list=list(db.articles.find({},{"_id"=0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!'})