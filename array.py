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

print("list after removing duplicates",unique)      '''

# sort in ascending and descending
arr = list(map(int,input("Enter elements:  ").split()))

arr.sort()
print("acsending: ",arr)

arr.sort(reverse=True)
print("descending: ",arr)

