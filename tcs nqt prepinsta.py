# moves all the zeroes to the end
'''arr = list(map(int, input("enter  th elements: ").split()))

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
     arr[pos],arr[i] = arr[i],arr[pos]
     pos += 1

print("AFTER MOVING ALL THE ZEROES TO THE END:",arr)  

# decimal to binary

n = int(input("enter elements: "))     # n = 10  , n.bit_length() = 10 -> 1010 -> 4 bits
print((1 << n.bit_length()) - 1 - n)   # 1 << 4 , 1010 -> 100000 -> 16 -> 16-1 -> 15 - 10 -> 5'''

# counting days problem

def count_sundays(start_day , n):
    days = {"mon": 0, "tue": 1, "wed": 2, "thur": 3, "fri": 4, "sat": 5, "sun": 6 }

    start_index = days[start_day.lower()]

    #days to reach first sunday
    days_to_sunday = (6 - start_index) % 7

    # if no sunday within n days
    if days_to_sunday >= n:
        return 0
    
    #count sundays
    remaining_days = n - days_to_sunday
    return 1 +(remaining_days // 7)

#example
print(count_sundays("tue",20))
