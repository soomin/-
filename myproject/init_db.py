import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# DB에 저장할 영화인들의 출처 url을 가져옵니다.
def get_urls():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    urls = []
    for i in range(1,6):
        
        data = requests.get(f'http://www.catpang.com/shop/goods/goods_list.php?category=001001001&searchOption%5B0%5D=7&scroll=0&brandType&sort=price_hign&page={i}', headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        trs = soup.select('div.list-wrap> ul >li >div.item-info> a:nth-child(1)')
    
        # print(trs)
   
        
        for tr in trs:
            # print('tr is', tr)
            if tr is not None:
                baseurl = 'http://www.catpang.com'
                url = baseurl + tr['href']

                # print(url)
                urls.append(url)

    return urls

# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 콜렉션에 저장합니다.
def insert_star(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    names = soup.select_one('div.sell-wrap> h2> #viewName').text
    # print(names)
    
    price = soup.select_one ('dl.price-sell> dd> strong.num').get_text()
    # print(price)
    image_url = soup.select_one ('div.photo-sell-wrap>div.photo-wrap>div.photo-view>img')['src']
    # print(image_url)

    ingredients = soup.select('#content_view_desc > .add-info')
    ingredi = ''
    for ingredient in ingredients:
        if "원료구성" in ingredient.text:
            ingredi = ingredient.text
            
    wheksqor = soup.select('#content_view_desc > .add-info')
    eksqor=''
    for wheks in wheksqor:
        if "조단백" in wheks.text:
            eksqor = wheks.text.split(',')
            
            
        print(eksqor)
            
    img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
    recent = soup.select_one(
        '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

    doc = {
        'img_url' : image_url,
        'name': names,
        'price': price,
        'ingredient': ingredi,
        
        
    }

    # db.saryo.insert_one(doc)
    # print('완료!')

# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
# def insert_all():
#     db.saryo.drop()  # mystar 콜렉션을 모두 지워줍니다.
    
#     urls = get_urls()
#     for url in urls:
#         insert_star(url)


# ### 실행하기
# insert_all()