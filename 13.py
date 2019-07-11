v=int(input())
b=v
s=0
while v!=0:
  d=v%10
  s=s*10+d
  v=v//10
if(s==b):
  print('yes')
else:
  print('no')
