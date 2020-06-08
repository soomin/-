from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

movie=db.movies.find_one({'title':'매트릭스'})
movie_star = movie['star']
# print(movie_star)

same_star_movies=list(db.movies.find({'star':movie_star}))

for same_star_movie in same_star_movies:
    wpahr=same_star_movie['title']
    print(wpahr)

    db.movies.update_many({'star':movie_star},{'$set': {'star':0} })