def f1(n):
  if n>0:
    f1(n-1)
    no=n*2-1
    print(no)

f1(10)    