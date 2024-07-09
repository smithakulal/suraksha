import random
import time
s=time.time()
c=100
l=[]
for j in range(c):
  randomno=random.randint(1,10)
  l.append(randomno)
print('l=',l)
key=random.randint(1,100)
print('key=',key)
i=0
while i<c:
 if key==l[i]:
  print('found at position',i)
  break
 i=i+1
else:
 print('not found')

e=time.time()
tt=e-s
print('timetaken=',tt)

l.sort()
print('l=',l)

sa=time.time()
left=0
right=len(l)-1
result=-1

while left<=right:
 mid=(left+right)//2

 if l[mid]==key:
  result=mid
  break
 elif l[mid]<key:
   left=mid+1
 else:
  right=mid-1

if result!=-1:
 print('found at position',result)
else:
 print('not found')
en=time.time()
tt2=en-sa
print('timetaken=',tt2)
