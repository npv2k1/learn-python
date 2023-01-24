import requests
a = requests.get("https://www.office.com/?auth=2")
print(a.status_code)
f=open('a.html','wb')
f.write(a.content)
f.close()
print(a.cookies)

# cookies={}
# with open('b.html','wb') as f:
   
#     b=requests.get("https://www.office.com/login?es=Click&amp;ru=%2F",cookies=a.cookies)
#     print(b.status_code)
#     f.write(b.content)
    


#print("Cookies"+a.cookies)
