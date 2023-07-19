def create_a_file():
    lines = []
    for i in range(6):
        line = input("Enter the line:")
        lines.append(line)
    
    file_name = "neeraj.txt"
    with open(file_name,'w') as file:
        file.writelines(lines)
    
    return file_name

def count_uppercase_lowercase_digits(file_name):
    uc = 0
    lc = 0
    dig = 0
    
    with open(file_name,'r') as file:
        contents = file.read()
        
        for char in contents:
            if char.isupper():
                uc = uc + 1
            elif char.islower():
                lc = lc + 1
            elif char.isdigit():
                dig = dig + 1
    return uc,lc,dig

def read_contents(file_name):
    with open(file_name,'r') as file:
        contents = file.read()
        print(contents)
file_name = create_a_file()
u,l,d = count_uppercase_lowercase_digits(file_name)
print(u)
print(l)
print(d)
