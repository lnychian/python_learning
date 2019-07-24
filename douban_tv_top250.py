import requests
import json
import pymongo
client = pymongo.MongoClient(host='localhost',port=27017,connect=False)
douban = client['douban']
douban.authenticate(name='douban_user',password='123456')
douban_tv = douban['douban_tv']
douban_tv.create_index([('id',1)],unique=True)
# url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=0'
urls = ['https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start='+ str(n) for n in range(0,250,25)]
"""
https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=0
https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=20
"""

for url in urls:
    response_data = requests.get(url)
    json_data = json.loads(response_data.text)
    for tv in json_data['subjects']:
        data = {
            'rate':tv['rate'],
            'title':tv['title'],
            'img_url':tv['cover'],
            'id':tv['id'],
            'tag':"美剧"
        }
        douban_tv.insert_one(data)
        print(data)