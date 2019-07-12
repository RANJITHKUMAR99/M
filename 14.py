a=int(input())
b=0
if a<=1:
  print("invalid")
elif a==2:
  print('yes')
else:
  for i in range(2,a):
    if(a%i==0):
      b=0
      break
    else:
      b=1
  if b==0:
    print("no")
  else:
    print("yes")
