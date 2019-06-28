a=input().split()
b=int(a[0])
c=int(a[1])
l=[]
for i in range(b):
    d=int(input())
    l.append(d)
s=0
for i in range(0,c):
    s=s+l[i]
print(s)
