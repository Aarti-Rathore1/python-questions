 # find maximum and minimum of array 
'''arr = list(map(int,input("Enter numbers separated by spaces: ").split()))

Maximum = arr[0]
Minimum = arr[0]

for num in arr:
    if num > Maximum:
        Maximum = num

    if num < Minimum:
        Minimum = num

print("maximum: ",Maximum)
print("Minumum: ",Minimum)      

# reverse a array without using extra space

arr = list(map(int,input("Enter numbers using spaces: ").split()))

start = 0
end = len(arr)-1

while start < end :
    arr[start],arr[end] = arr[end],arr[start]

    start += 1
    end -= 1

print("reverse array is : ",arr)


# second largest element
arr = list(map(int, input("Enter elements separated by space: ").split()))

arr.sort()

print("second largest element: ",arr[-2])


# check if arrray is not sorted 
arr = list(map(int,input("Enter elements with spaces: ").split()))

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
          return False
    return True

if  is_sorted(arr):
   print("array is sorted")

else:
   print("array is not sorted") 

#   moves all the zeros to the back of the array
arr = list(map(int,input("Enter the elements with spaces: ").split()))

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print("After moving zeros: ",arr)        


# count frequency of each element
arr = list(map(int,input("Enter elements with spaces: ").split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("frequencies: ")
for key,value in freq.items():
    print(key,"->",value)  


#shorter way
from collections import Counter

arr = list(map(int,input("Enter the elements: ").split()))
freq = Counter(arr)

print(freq)

#   find a element in linear search
arr = list(map(int, input("Enter the elements with spaces: ").split()))

key = int(input("Enter the number which you want to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("number found at index",i)
        found = True
        break

if not found:
  print("number not found")    

#count occurence using linear search

arr = list(map(int,input("Enter elements using spaces: ").split()))
key = int(input("Enter the element you want to count: "))

count = 0

for num in arr:
   if num == key:
      count += 1

print("Number appears",count,"times")    

# find all negative number

arr = list(map(int,input("Enter the elements: ").split()))
negatives = []

for num in arr:
    if num < 0 :
        negatives.append(num)

if negatives:        
        print("Negative numbers are: ",negatives)
       
else:
    print("No negative numbers")    


# search for name in a list
names  = input("Enter names separated by spaces: ").split()
key  = input("Enter name to search: ")

found = False

for i in range(len(names)):
    if names[i].lower() == key.lower():
        print("name found at index",i)
        found = True
        break

if not found:
    print("name not found") 

# find index using binary search

arr = list(map(int,input("Enter the elements in sorted way: ").split()))
key = int(input("Enter the element: "))

low = 0
high = len(arr) - 1
found = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
      found = mid
      break
    elif arr[mid] < key:
       low = mid + 1
    else:
       high = mid - 1

print("Index: ",found)      

# first occurence using binary search

arr = list(map(int,input("Enter the elements in sorted array: ").split()))
key = int(input("Enter the element to search: "))

low = 0
high = len(arr)-1
result = -1

while low <= high:
   mid = (low + high) // 2

   if arr[mid] == key:
    result = mid
    high = mid -1       # move left to find earlier occurence

   elif arr[mid] < key:
      low = mid + 1
   else: 
      high = mid -1 

print("First occurence index: ",result)    

# find last occurence
arr = list(map(int,input("Enter the elements in sorted array: ").split()))
key = int(input("Enter the element: "))

low = 0
high = len(arr) - 1
result = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        result = mid
        low = mid + 1

    elif arr[mid] < key:
        low = mid + 1

    else :
        high = mid - 1

print("Index: ",result)   

# count total  occurence
def first_occurence(arr,key):
    low = 0
    high = len(arr)-1
    result = -1 

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result
                
def last_occurence(arr,key):
    low = 0
    high = len(arr)-1
    result = -1 

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            low  = mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result

arr = list(map(int,input("Enter the elments with spaces: ").split()))
key = int(input("Enter numbers to count: "))

first = first_occurence(arr,key)
last = last_occurence(arr,key)

if first == -1:
    print("count: 0")
else:
    print("count:",last - first + 1)    

# search insert position 
arr = list(map(int,input("enter the elemnts in sorted way: ").split()))
key = int(input("Enter the element: "))

low = 0
high = len(arr) - 1
ans = len(arr)

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        ans = mid
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1

print("position: ",ans)        

# reverse a string
s = input("Enter a string: ")

i = len(s) - 1
rev = ""

while i >= 0:
    rev += s[i]
    i -= 1

print("reversed string: ",rev) 

# check if number is palindrome
s = input("Enter a string: ").lower()

i = 0 
j = len(s) - 1
is_palindrome = True

while i < j :
    if s[i] != s[j]:
     is_palindrome = False
     break

    i += 1
    j -=1 

if is_palindrome :
     print("palindrome")

else:
    print("non palindrome")     

# count consonants and vowels in a string

s = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for ch  in s:
    if ch.isalpha():       # only count letters
        if ch in "aeiou":
            vowels += 1

        else:
            consonants += 1

print("vowels: ",vowels)
print("consonants: ",consonants)   

# remove all spaces from a string

s = input("Enter a string: ")

result = ""
for ch in s:
    if ch != " ":
        result += ch
print("without space: ",result)

# convert uppercase <-> lowercase
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print("converted string: ",result)     

#  arraylist
n = int(input("how many elements: "))      
arr = []

for i in range(n):
    x = int(input())
    arr.append(x)

print(arr)  

# update an element at a given index

arr = list(map(int,input("Enter list element: ").split()))
print("original list: ",arr)

index = int(input("Enter index to update: "))
new_value = int(input("Enter new value: "))

if 0 <= index < len(arr):
    arr[index] = new_value
    print("updated list: ",arr)

else:
    print("invalid index")   

# remove element from pythonlist
arr = list(map(int,input("Enter the elments: ").split()))
print("original  list: ",arr)

choice = int(input("enter 1 to remove by index,enter 2 to remove by value: "))

if choice == 1:
    index = int(input("Enter index to remove: "))
    if 0 <= choice <len(arr):
        arr.pop(index)
        print("updated array : ",arr)

    else:
        print("invalid index")

elif choice == 2:
    value = int(input("Enter element to remove: "))
    if value in arr:
        arr.remove(value)
        print("updated list: ",arr)

    else:
        print("value not found")
        

else:
    print("invalid choice")    

#remove duplicates in pythonlist
arr = list(map(int,input("Enter list elements: ").split()))

unique = []
for x in arr:
   if x not in unique:
      unique.append(x)

print("list after removing duplicates",unique)      

# sort in ascending and descending
arr = list(map(int,input("Enter elements:  ").split()))

arr.sort()
print("acsending: ",arr)

arr.sort(reverse=True)
print("descending: ",arr)

# two sum problem(return indices)
arr = list(map(int,input("enter elements:").split()))
target = int(input("enter target sum: "))

seen = {}

for i in range(len(arr)):
    need = target - arr[i]

    if need in seen:
        print("Indices:",seen[need],i)


    seen[arr[i]] = 1      

# rotate array by k positions
def rotate_right(arr,k):
    n = len(arr)
    k %= n

    def reverse(l,r):
        while l < r:
            arr[l],arr[r] = arr[r],arr[l]
            l += 1
            r -= 1

    reverse(0, n - 1)  # reverse whole array
    reverse(0, k - 1)    # reverse first k
    reverse(k, n -1)   # reverse rest   

arr = [1,2,3,4,5]
rotate_right(arr,2)
print(arr)

# union and intersection of two array

def union_and_intersection(a,b):
    setA = set(a)
    setB = set(b)

    union = list(setA | setB)
    intersection = list(setA & setB)

    return union, intersection
A = [1,2,3,4,5]
B = [3,4,5,6,7]
u,i = union_and_intersection(A,B)
print("union: ",u)
print("intersection:",i)

# finding missing numbers from 1 to n
arr = list(map(int,input("Enter numbers from 1 to n (one missing): ").split()))
n = int(input("enter n: "))

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing = expected_sum - actual_sum
print("Missing number: ",missing) 

# sort 0's, 1's, 2's
arr = list(map(int,input("enter 0's, 1's, 2's: ").split()))

low = 0
mid = 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1

    elif arr[mid] == 1:
        mid  += 1

    else:           # arr[mid] == 2
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1
        
print("sorted array: ",arr)      

# subarray with given sum (sliding window)

arr = list(map(int,input("enter non -negative numbers: ").split()))
target = int(input("enter target sum:"))

left = 0
current_sum = 0
found = False

for right in range(len(arr)):
    current_sum += arr[right]

    while current_sum > target and left  <= right:
        current_sum -= arr[left]
        left += 1

    if current_sum == target:
        print("subarray found from index",left,"to",right)
        found = True
        break

if not found:
    print("no subarry found")   



# longest common prefix 

def longestCommonprefix(strs):
    if not strs:
        return ""
    
    prefix =  strs[0]

    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
            
    return prefix     

arr = ["flower","flow","flight"]
print(longestCommonprefix(arr))   

# count frequency of characters using hashmap

def countfrequency(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] = 1
        else:
            freq[char] = 1

    return freq

string = "programming"
print(countfrequency(string))

# anagram check
def is_anagram(s1 ,s2):
    if len(s1) != len(s2):
        return False
    
    freq = {}

    for ch in s1:
        freq[ch]  = freq.get(ch,0) + 1
         

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0  

print(is_anagram("listen","silent"))          

# remove duplicates from string

def remove_duplicates(s):
    result = ""

    for ch in s:
        if ch not in result:
            result += ch

    return result   

print(remove_duplicates("programming"))   

# find first non repeating character

def first_non_repeating(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch,0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch
        
    return None

print(first_non_repeating("aabbccdefHHjj"))    

# string compresion

def compressString(s):
    if not s:
        return ""
    
    result = ""
    count = 1

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1

    result += s[-1] + str(count)

    return result
print(compressString("aaabbbbbbcdee"))        

# merging two sorted string

def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
            
        else:
            result.append(list2[j])
            j += 1
           
     # adding remaining elements
    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1      

    return result
        
print(merge_sorted_lists([1,3,5],[2,4,6]))
print(merge_sorted_lists([1,4,5],[2,8,7]))
print(merge_sorted_lists([],[9,3,5]))
print(merge_sorted_lists([1,2,3],[]))
print(merge_sorted_lists([-3 ,-4,5],[-1,2,3]))

# commmon between two list

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1,2,3,4],[1,34,4,5]))

# pascal's triangle

def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)    # first and last element are 1

        for j in range(1 , i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle .append(row)

    return triangle

# example usage
n = 5
triangle = generate_pascals_triangle(n)

for row in triangle:
    print(row) 


# kadane's algorithm (maximum subarray sum)
def kadane(nums):
    current_sum = nums[0]
    max_sum  = nums[0]

    for x in nums[1:]:
        current_sum = max(x,current_sum + x)
        max_sum = max(max_sum,current_sum)

        return max_sum
    
arr = [-2, 1, -3, 4, 4,1,  -1, 2, 1, -5, 4]
print("running kadane file")
print(kadane(arr)) '''

# set matrix zeros 
def setZeroes(matrix):
    if not matrix or not matrix[0]:
        return
 
    r = len(matrix)
    c = len(matrix[0])
    rowtrack = [0 for _ in range(r)]
    coltrack = [0 for _ in range(c)]

    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
               rowtrack[i] =-1
               coltrack[j] =-1

    for i in range(0,r):
        for j in range(0,c):
            if rowtrack[i] == -1 or coltrack[j] == -1:
               matrix[i][j] = 0

matrix = [
    [1, 1, 1],
    [2, 0, 4],
    [5, 1, 6]
]            
setZeroes(matrix)
print(matrix)   










