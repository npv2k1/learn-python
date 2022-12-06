import requests
import time
from lxml import html
import re

'''
Các link tham khảo.
https://www.one-tab.com/page/33p0T7mGQqSgGIn1AP-Ryw
'''
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId=ds5ou53ha5p2lmdnprdcrasb',
    'Host': 'medianews.vn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
# a=requests.get('http://medianews.vn/Webcms/Websites/Blank?action=edit&qCode=1',headers=headers)
# tree=html.fromstring(a.content)
# csc=tree.xpath('//*[@id="txtqContent"]/text()')
#
# f=open('file.txt','w',encoding='utf-8')
#
# f.write(''.join(csc[0].split('\r')))
# f.close()
# print(csc)
for i in range(1, 1000):
    a = requests.get(
        f'http://medianews.vn/Webcms/Websites/Blank?action=edit&qCode={i}', headers=headers)
    tree = html.fromstring(a.content)

    csc = tree.xpath('//*[@id="txtqContent"]/text()')
    print(i)
    print(csc)
    if(len(csc) != 0):
        f = open('code 2/'+str(i)+'.txt', 'w', encoding='utf-8')
        f.write(''.join(csc[0].split('\r')))
        print("dowload: ", i)
        
        f.close()

    # Lấy số bài đã làm
    # csc = tree.xpath(
    #     '//*[@id="fromEdit"]/div[1]/table/tbody[1]/tr/td[5]/text()')
    # if(len(csc) != 0):
    #     print(csc)
    #     text = re.search(r'\[(\d+)\]',csc[2]).group(1)
    #     print(i,'  ',text)
    #     x=input()
    #     break;
