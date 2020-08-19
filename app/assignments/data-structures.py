simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
print(simple_list)

new_list = [True, False, True]
print(any(new_list)) #at least 1 value is True
print(all(new_list)) #all values should be true

#unpacking
list_1 = [1,2,3]
a, b, c = list_1

#assignment task1: create list of persons
people_list = [
    {'name': 'Anna', 'age': 25, 'hobbies': ['drawing', 'listening to the music', 'reading']},
    {'name': 'Max', 'age': 29, 'hobbies': ['running', 'swimming', 'reading']},
    {'name': 'Danny', 'age': 30, 'hobbies': ['writing poems', 'designing', 'photoshooting']}
]

people_names = [person['name'] for person in people_list]
print(people_names)

check_if_older_20 = all([person['age'] > 20 for person in people_list])
print(check_if_older_20)

people_list_copy = [person.copy() for person in people_list]
people_list_copy[0]['name'] = 'Iryna'
print(people_list_copy[0])
print(people_list[0])

user_1, user_2, user_3 = people_list
print(user_1)
print(user_2)
print(user_3)


