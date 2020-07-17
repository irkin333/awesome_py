simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
print(simple_list)

new_list = [True, False, True]
print(any(new_list)) #at least 1 value is True
print(all(new_list)) #all values should be true