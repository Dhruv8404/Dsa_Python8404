def f1(n):
    if n>0:
        f1(n-1)
        print(n)
f1(5)    