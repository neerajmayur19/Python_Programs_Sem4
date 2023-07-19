import random
arr = []
for i in range(20):
    value = random.randint(9,999)
    arr.append(value)
print(arr)
final_arr = []
for i in range(20):
    if (len(str(arr[i])) == 2 or len(str(arr[i]))==4):
        final_arr.append(arr[i])

print("The filtered values of the array which have length 2 and length 4")
print(final_arr)
