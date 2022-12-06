import requests
a = requests.get(
    "https://vicostone.com/vi-vn/investor-news/2020/11/thong-bao-lay-y-kien-co-dong-bang-van-ban")
with open('b.html','wb') as f:
    f.write(a.content)
