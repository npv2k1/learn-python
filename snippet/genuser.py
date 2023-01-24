i=1
while(i<=200):
	with open("user.txt",'a') as f:
		f.write('user'+str(i)+"@thptnewton.onmicrosoft.com"+'\n')
	i+=1