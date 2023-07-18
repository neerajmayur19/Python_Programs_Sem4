def add_words(dic):
    word = input("Enter the word:")
    meaning = input("Enter the meaning:")
    dic[word] = meaning
    print("Word added successfully")

def search_words(dic):
    key = input("Enter the word to be searched:")
    if key in dic:
        print(f"The Meaning of the {key} is {dic[key]}")
    else:
        print("No such word has been found")

def similar_meaning_words(dic):
    meaning = input("Enter the meaning:")
    found_words = []
    for word,word_meaning in dic.items():
        if word_meaning == meaning:
            found_words.append(word)
    print(found_words)

def remove_words(dic):
    word = input("Enter the word that you wish to remove:")
    if word in dic:
        del dic[word]
        print("word deleted successfully")
    else:
        print("Could not find the word")

def sort_dictionary(dic):
    sorted_words = sorted(dic.keys())
    for word in sorted_words:
        print(f"The meaning of the word {word} is {dic[word]}")

def display_menu():
    print("1.Add a word")
    print("2.Search a word and retrieve the meaning")
    print("3.Search words with a similar meaning")
    print("4.Remove a particular word")
    print("5.Sort the words alphabetically")
    print("6.Exit")
def main():
    
    dic = {}
    while True:
        display_menu()
        choice = int(input("Enter the choice:"))
        if choice == 1:
            add_words(dic)
        elif choice == 2:
            search_words(dic)
        elif choice == 3:
            similar_meaning_words(dic)
        elif choice == 4:
            remove_words(dic)
        elif choice == 5:
            sort_dictionary(dic)
        elif choice == 6:
            break
main()   
