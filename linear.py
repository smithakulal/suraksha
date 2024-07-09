import random
n=5
c=[20,40,60,8,100]
i=0
k=80


while i<n:
   if k==c[i]:
      print("key found")
      break
   i=i+1

else:
  print("not found")
print(i)
