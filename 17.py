a=input().split()
b=int(a[0])
c=int(a[1])
for i in range(b,c+1):
  if i>1:
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      print(i,end=" ")
