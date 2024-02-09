def fun(s1,s2):
 e=0
 pos=0
 neg=0
 for e in range(0,5):
    print(e+1," ",s1[e])
    str=input("enter word:")
    if str==s2[e]: 
        pos=pos+1
        print("positive",pos)
    else:
         neg=neg-1
         print("negative",neg)
 print("total score",pos+neg)
l1=["faerth","dinia","aus","eahrt","neiunro"]
l2=["father","india","usa","earth","ineuron"]
fun(l1,l2)