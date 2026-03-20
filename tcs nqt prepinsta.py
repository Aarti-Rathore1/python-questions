# moves all the zeroes to the end
arr = list(map(int, input("enter  th elements: ").split()))

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
     arr[pos],arr[i] = arr[i],arr[pos]
     pos += 1

print("AFTER MOVING ALL THE ZEROES TO THE END:",arr)  

# decimal to binary

n = int(input("enter elements: "))     # n = 10  , n.bit_length() = 10 -> 1010 -> 4 bits
print((1 << n.bit_length()) - 1 - n)   # 1 << 4 , 1010 -> 100000 -> 16 -> 16-1 -> 15 - 10 -> 5
