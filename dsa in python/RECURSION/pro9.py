def f1(n):
 if n<0:
  return 0
 
 so=n*2-1
 s=f1(n-1)+so
 
 return s

r=f1(3)    
print(r)