import requests
import re
import time
def mp3file(strin):
    while True:
        while True:
            Header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
                'Connection': 'keep-alive',
                'Content-Length': '187',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'speech.openfpt.vn',
                'Origin': 'https://fpt.ai',
                'Referer': 'https://fpt.ai/vi/tts-vi',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            }
            data = {
                'voice-type': 'new',
                'text': strin,
                'gender': 'myan',
                'speed': '0',
            }
            a = requests.post('https://speech.openfpt.vn/speech', data=data, headers=Header)
            print(a)
            try:
                res = re.search(r'"Url":"(.*?)"', a.text)
            except:
                continue
            try:
                urlmp3 = str(res.group(1))
            except:
                continue
            break
        print(urlmp3)
        mp3 = requests.get(urlmp3)
        print(mp3.status_code)
        if (mp3.status_code == 200):
            f = open(strin + '.mp3', 'wb')
            f.write(mp3.content)
            f.close()
            print("*******************")
            break
        else:
            mp3file(strin)
            break
#srcsub=open('subsrc.txt','r',encoding='UTF-8')
#listsub=srcsub.read().split('\n')
# while True:
#     mp3file(listsub[i])
#     i=i+1
#     if(i==len(listsub)):
#         break
#     print("..........Continue.........")

# for i in listsub:
#     if(len(i)==0):
#         continue
#     print(i)
#     mp3file(str(i))
while True:
    a=input("moi ban nhap chuoi: ")
    mp3file(a)
