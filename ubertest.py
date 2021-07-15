'''try:
	l= list(map(int,input().split()))
	x=int(input())
	count=0
	for i in range(0,len(l)):
		for j in range(0,len(l)):
			if i!=j:
				if str(x)==str(l[i])+str(l[j]):
					count+=1
				if str(x)==str(l[j])+str(l[i]):
					count+=1
	print(count//2)
except:
	pass
'''
def diceTotalScore(a, b, c):
    1<=a<=6
    1<=b<=6
    1<=c<=6
    tempa = 0
    tempb = 0
    tempc = 0
    result = 0
    for i in range(a):
        tempa = i
    for j in range(b):
        tempb = j
    for k in range(c):
        tempc = k
    if(a==b==c):
        result = 1000*a
        return result;
    else if(a==b|b==c|c==a):
        x = a==b|b==c|c==a
        result = 500*x
        return result;
    else:
		result = 100*min(a,b,c)
		return result;