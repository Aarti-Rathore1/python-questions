# moves all the zeroes to the end
arr = list(map(int, input("enter  th elements: ").split()))

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
     arr[pos],arr[i] = arr[i],arr[pos]
     pos += 1

print("AFTER MOVING ALL THE ZEROES TO THE END:",arr)    
