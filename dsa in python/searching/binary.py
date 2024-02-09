def binarySearch(mylist, search):
    mylist.sort()
    high = len(mylist) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        
        if mylist[mid] > search:
            high = mid - 1

        elif mylist[mid] < search:
            low = mid + 1
        elif mylist[mid] == search:
            return mid
    return -1  # Return -1 if the element is not found

my_list = list(map(int, input("Enter the list of numbers separated by space: ").split()))
search_ele = int(input("Enter the number to search: "))

result = binarySearch(my_list, search_ele)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")