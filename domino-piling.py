def domino(m,n):
	if ((n>=1 and n<=16) and (m>=1 and m<=16)):
		area=m*n
		dom=2
		doms=area//2
		return doms
