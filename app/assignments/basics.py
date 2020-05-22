def print_user_data(name, age):
    print('User name is ' + name + ' and age is ' + age)
    decades = int(age)//10
    print('User lived for ' + str(decades) + ' decades!')


print_user_data(age=input('Please, enter your age: '), name='Ira')