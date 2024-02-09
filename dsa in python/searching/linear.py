def linear(mylist,search):
    for i in range(len(mylist)):
        if search == mylist[i]:
            return i  # Return the index if the element is found
       
mylist = list(map(int, input("Enter the list of numbers ").split()))
search = int(input("Enter the number to search: "))

result = linear(mylist, search)
print(result)