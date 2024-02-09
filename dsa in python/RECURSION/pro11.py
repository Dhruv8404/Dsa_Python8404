def f1(n):
    if n==1:
      return 1
    so=n**2
    s=f1(n-1)+so
    return s
r=f1(12)    
print(r)