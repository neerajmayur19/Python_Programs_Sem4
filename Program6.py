def max_min(lst):
    maximum = lst[0]
    minimum = lst[0]
    for i in range(len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]
        if lst[i] < minimum:
            minimum = lst[i]
    print(f"The Maximum element of the array is {maximum} and the minimum value of the array is {minimum}")
    return maximum

def second_largest(lst,maximum):
    second = lst[0]
    for i in range(len(lst)):
        if lst[i]<maximum and lst[i]>second:
            second = lst[i]
    print(f"The second largest value of the array is {second}")

lst = [23,45,-9,0,43,98]
maxine = max_min(lst)
second_largest(lst,maxine)
        
