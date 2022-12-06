f = open('sortmail.txt', 'r')
setmail =set(f.read().split('\n'))
dict_mail_len={}
for i in setmail:
    try:
        dict_mail_len[len(i)]+=[i]
    except:
        dict_mail_len[len(i)]=[i]
print(dict_mail_len)
res=open('res.txt','w')
res.write(str(dict_mail_len))
