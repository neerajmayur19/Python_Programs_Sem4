subjects = input("Enter the subjects seperated by a space")
lst = subjects.split()

def print_subjects(lst):
    for i in range(len(lst)):
        print(lst[i])

def print_second_and_fifth_element(lst):
    print(lst[1])
    print(lst[4])

def print_first_4_elements(lst):
    for i in range(4):
        print(lst[i])

def print_last_4_elements(lst):
    for i in range(1,5):
        print(lst[-i])

def search(lst):
    if "PythonProgrammingLab" in lst:
        print("Yes it contains")
    else:
        print("No it does not contain")

def demo_of_append_and_insert(lst):
    lst.append("PPE")
    print(lst)
    lst.insert(1,"PPE")
    print(lst)

def demo_of_remove_and_pop(lst):
#remove basically deletes the first occurence of a particular element but pop removes the element in a particular index
    lst.remove("CS42")
    print(lst)
    lst.pop(1)
    print(lst)
    
#Just call all the functions one by one to show how it works
