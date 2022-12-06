import requests

dml= list(open("domain.txt",'r').read().split('\n'))

for i in dml:
    print(i)
    a = requests.get(
        f'https://www.whatsmydns.net/api/details?server=324&type=MX&query={str(i)}')
    with open("res.txt", 'a') as f:
        f.write(str(a.content)+'\n')
