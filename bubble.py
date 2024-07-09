import time
a=[56,76,32,1,9,43]
n=len(a)
j=n-1
st=time.time()
while j>=0:
	i=0
	while i<j:
		if a[i]>a[i+1]:
		  temp=a[i]
		  a[i]=a[i+1]
		  a[i+1]=temp
		i=i+1
	j=j-1
print(a)
et=time.time()
print("execution time: {:3f} seconds" .format(et-st))
