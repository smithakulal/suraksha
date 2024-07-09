def search(a,k):
 for i in range(len(a)):
  if a[i]==k:
   return i
 return -1
a=(10,20,30,40,50)
k=int("Enter an element")
result=search(a,k)
if result==-1:
 print("k is not present in array")
else:
 print("k is present in array")
