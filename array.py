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

print("second largest element: ",arr[-2])'''


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

    