a1=input().split()
b=int(a1[0])
c=int(a1[1])
d1=0
for i in range(b,c+1):
  if i>1:
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      d1=d1+1
print(d1)
