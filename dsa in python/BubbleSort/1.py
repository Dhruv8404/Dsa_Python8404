
'''def calculate_power(m, n):
    # Case 1: Both m and n are positive integers
    if isinstance(m, int) and isinstance(n, int) and m > 0 and n >= 0:
        return m ** n

    # Case 2: m is a positive integer, and n is a negative integer
    elif isinstance(m, int) and isinstance(n, int) and m > 0 and n < 0:
        return 1 / (m ** abs(n))

    # Case 3: m is 0, and n is any integer (except 0)
    elif m == 0 and isinstance(n, int) and n != 0:
        return 0

    # Case 4: m is any non-zero real number, and n is a positive or negative integer
    elif isinstance(m, (int, float)) and isinstance(n, int):
        return m ** n

    # Case 5: All other cases
    else:
        return 0  # Indicate that the input is not supported

# Examples
print(calculate_power(0, 2))      # Output: 8
print(calculate_power(0, 2.5))     # Output: 0.125
print(calculate_power(5, 0))      # Output: 0
print(calculate_power(3.5, 0))    # Output: 12.25
print(calculate_power(6, 4.25))    # Output: None (unsupported input)
print(calculate_power(14,3))


'''
'''

s1=[1,2,3,4,5,6]
s2=[2,11,7,8,9,10]

for i in s1:
    temp=i
    for j in s2:
       if temp==j:
           s2.remove(j)
           print(j)
        
def replace_elements(s1, s2):
    # Clear the contents of s1
    s1.clear()
    
    # Copy elements from s2 to s1
    s1.extend(s2)

# Example usage:
s1 = [1, 2, 3, 4]
s2 = [5, 6, 7, 8]

print("Before replacement:")
print("s1:", s1)
print("s2:", s2)

replace_elements(s1, s2)

print("\nAfter replacement:")
print("s1:", s1)
print("s2:", s2)'''    
"""
x=input("enter no::")
temp =x[::-1]
print(temp)
"""
'''
m = {'z': 1, 'x': 2, 'y': 3}
s = "zzxxyy"
ans = 0

for i in range(len(s)):
   for j,k in m.items():
    if s[i] == j:
      ans=k+ans
print(ans)

'''


'''
s = ["flower","flow","flight"]

ans=""
s=sorted(s)
first=s[0]
last=s[-1]
for i in range(min(len(first),len(last))):
  if first[i]==last[i]:
    ans=ans + first[i]  
  else:
    ans="None"  
print(ans)  
'''
"""
strs = ["flower","flow","floght"]
ans=""
s=sorted(strs)

first = s[0]
last = s[-1]
for i in range(min(len(first),len(last))):
    if first[i]==last[i]:
        ans+=first[i]
print(ans)  
"""
"""
def sum(list):
    maxele=0
    minele=0
   

    for i in list[1:]:
      maxele=max(maxele,i-list[1])
      
   
    if  maxele >0:
       print(maxele)
    else:
       print(minele) 
      
list=[7,6,4,3,1]
sum(list)
"""
"""
def max_subarray_sum(nums):
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print(result)

"""

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check which side is sorted
        if nums[left] <= nums[mid]:
            # Left side is sorted

            # Check if the target is in the left side
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right side is sorted

            # Check if the target is in the right side
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1  # Target not found

# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search(nums, target)
print(result)
