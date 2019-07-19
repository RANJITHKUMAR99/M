a1=input().split()
b1=a[0]
c1=a[1]
d1=0
for i in range(0,len(b1)):
    if b1[i]!=c1[i]:
        d1=d1+1
if d1==1:
    print("yes")
else:
    print("no")
