def sort_by_length(strs):
    tuples = [(string,len(string)) for string in strs]
    sorted_tuples = sorted(tuples, key = lambda x:x[1])
    return sorted_tuples



names = input("Enter the names one after one seperated by a space")
lst = []
lst = names.split()
sorted_tuples = sort_by_length(lst)
print(sorted_tuples)
