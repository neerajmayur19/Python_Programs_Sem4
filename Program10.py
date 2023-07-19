def create_file():
    lines = [] 
    for i in range(5):
        line = input("Enter a line of the text:")
        lines.append(line)
    
    file_name = "neeraj.txt"
    with open(file_name,'w') as file:
        file.writelines(lines)
    
    return file_name

def compute_longest_and_shortest_word(file_name):
    with open(file_name,'r') as file:
        text = file.read()
        words = text.split()
        
        longest_word = max(words,key=len)
        shortest_word = min(words,key=len)
        
        return longest_word,shortest_word
file_name = create_file()
longest,shortest = compute_longest_and_shortest_word(file_name)

print(f"The longest word is {longest}")
print(f"The lenth of the longest word is {len(longest)}")
print(f"The shortest word is {shortest}")
print(f"The length of the shortest word is {len(shortest)}")
