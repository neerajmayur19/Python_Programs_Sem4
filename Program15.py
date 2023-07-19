try:
    lst = []
    for i in range(5):
        i = int(input("Enter the number:"))
        lst.append(i)
    print(lst[6])
    value = lst[4]/lst[0]
    print(value)

except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("No Exceptions")
finally:
    print("End of the program")
