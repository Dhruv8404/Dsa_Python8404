def f1(n):
 if n<=1:
  return 2
 f1(n-1)    
 so=n*2
 s=f1(n-1)+so
 
 return s
 

r=f1(3)
print(r)