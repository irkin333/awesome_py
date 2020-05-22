users_list = ['Anna', 'Jonh', 'Irina', 'Maximillian', 'Ziggy']

for user in users_list:
    if len(user) > 5:
        print(user + ' - this name is longer than 5 characters')

    if 'a' in user or 'A' in user:
        print(user + ' - this name has Aa character(s)')

while len(users_list) > 0:
    users_list.pop()

print(len(users_list))
print('Done!')
