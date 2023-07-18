def print_dictionary_values(dic):
    print(dic)
    print(dic.keys())
    print(dic.values())

def change_the_pw(dic):
    username = input("Enter the username for which you have to change the password:")
    if username in dic:
        pw = input("Enter the new password:")
        dic[username] = pw
    else:
        print("No such username has been found")

def get_the_password(dic):
    username = input("Enter the username for which you have to get the password:")
    if username in dic:
        print(f"The password for the username {username} is {dic[username]}")
    else:
        print("No such username was found")


dic = {"rahul": "genius", "kumar": "smart", "ankita": "intelligent"}
print_dictionary_values(dic)
get_the_password(dic)
change_the_pw(dic)
print_dictionary_values(dic)
