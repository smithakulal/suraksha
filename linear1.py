import random
import time
n=100
randomlist=[]
s=time.time()
for i in range(0,1000):
	n=random.randint(0,100)
	randomlist.append(n)
print(randomlist)
k=random.randint(1,100)
i=0
while i<len(randomlist):
   if k==randomlist[i]:
      print(k,"key found")
      break
   i=i+1
else:
   print("key is not found")
e=time.time()
total=e - s
print("time taken=",total)
print("generated")
plt.title("random numbers")
plt.xlabel("number of random number")
plt.ylabel("time(seconds)")
plt.show()
