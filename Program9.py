def add_an_item(t,item):
    t = t + (item,)
    return t 
    
def length_of_tuple(t):
    length = len(t)
    print(f"The length of the tuple is {length}")

def checking(t):
    item = input("Enter the item you want to search for in the tuple:")
    if item in t:
        print("The item is present in the tuple!")
    else:
        print("The following item is not found in the tuple")

def accessing_the_elements(t,index):
    if index <= len(t):
        value = t[index]
        print(f"The value present at the index {index} is {value}")
    else:
        print("Index is excessding the length of the tuple")

t = ('neeraj','mayur','sree')
t = add_an_item(t,'nidhi')
length_of_tuple(t)
checking(t)
accessing_the_elements(t,2)
