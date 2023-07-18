a = int(input("Enter the lower number of the range"))
b = int(input("Enter the upper number of the range"))
i = a
flag = True
while i<=b:
    for j in range(2,i):
        if i%j == 0:
            flag = False
            break
    if flag == True:
        print(i)
    flag = True
    i = i + 1
print("This is the end")
