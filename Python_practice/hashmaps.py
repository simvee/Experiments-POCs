from collections import defaultdict

# dict_of_lists = defaultdict(list)

dict_of_lists = {}

dict_of_lists.update({1: ['a']})
dict_of_lists[1].append(2)

print(dict_of_lists[1])