def f1(n):
 if n==0:
  return 1
   
 s=n+f1(n-1)
 return s

r=f1(10)
print(r)