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

print("First occurence index: ",result)  '''    

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


    