a=int(input("enter of num"))
n=[1,2,3,4,5,6,7]
k=int(input("enter a key"))
i=0
while i<a:
    if k==n[i]:
       print("found at", i,"th position")
       break
    i=i+1
else:
    print("key is not found")
  
