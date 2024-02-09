def bubble_sort(data_list):
    for e in range(1,len(data_list)):
        for i in range(len(data_list)-e):
               if data_list[i]>data_list[i+1]:
                     data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
l=[11,2,3,7,4,5,8,10]
bubble_sort(l)
print(l)


def modify_bubble_sort(list):
     flag=False
     for e in range(1,len(list)):
          flag=False
          for i in (len(list)-e):
               if list[i]>list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]
                    flag=True
          if not flag:
              break           

l=[1,2,3,7,4,5,8,11,11]
bubble_sort(l)
print(l)

def selection_sort(list):
  n=len(list)
  for i in range(n):
       min_index=i
       for j in range(i+1,n):   #  J   go to 1 to 10 
            if list[j]<list[min_index]:
                 min_index=j
       list[i],list[min_index]=list[min_index],list[i]                      

l=[1,2,3,7,4,5,8,11,11]
selection_sort(l)
print(l)   

def insertion_sort(list):
     for i in range(1,len(list)):
           temp=list[i]

           j=i-1
           while j>=0 and temp<list[j]:
                list[j+1]=list[j]
                j-=1
           list[j+1]=temp     
l=[1,2,3,7,4,5,8,11,11]
insertion_sort(l)
print(l)              


def Quick_sort(list):
     if len(list)<=1:
        return list
     else:
          
          loc=list[0]
          lesser=[x for x in list[1:] if x<=loc ]
          Grater=[x for x in list[1:] if x>loc ]
          
          return Quick_sort(lesser)+[loc]+Quick_sort(Grater)

l1=[18,93,46,11,34,35,56,34]
l1=Quick_sort(l1)
print(l1)


def Merge_sort(list):
     if len(list)>1:
          min =len(list)//2
          leftlist=list[:min]
          rightlist=list[min:]
          Merge_sort(leftlist)
          Merge_sort(rightlist)

          i,j,k=0,0,0 
          while i<len(leftlist) and j<len(rightlist):
               if leftlist[i] < rightlist[j]:
                    list[k]=  leftlist[i]
                    i+=1
               else:
                    list[k]=  rightlist[j]

                    j+=1  
               k+=1

          while i<len(leftlist):
                list[k]=  leftlist[i]
                i+=1
                k+=1

          while j<len(rightlist):
                list[k]=  rightlist[j]
                j+=1
                k+=1
          return list      
mylist=[9,39,47,1,47,8,93,957,686]
mylist=Merge_sort(mylist)
print(mylist)               