raw_header = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: vi,en-US;q=0.9,en;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 123
Content-Type: application/x-www-form-urlencoded
Cookie: wordpress_test_cookie=WP+Cookie+check
Host: portal.ptit.edu.vn
Origin: https://portal.ptit.edu.vn
Referer: https://portal.ptit.edu.vn/wp-login.php
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36
'''
result={}
for i in raw_header.split('\n'):    
    t=i.split(':')
    if len(t)==2:
       result[t[0].strip()]=t[1].strip()
print(result)