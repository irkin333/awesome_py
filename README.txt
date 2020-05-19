This is course project, built during my python learning.
Python types:
- Number:
    1. integer => 1, 5, 10  (use int() function to convert type to number int)
    2. float => 1.1, 5.8, 10.56  (use float() function to convert type to number float)
    easy to read way to write number: num = 1_000_000
- Boolean
- Sring
- Dictionaries
- Objects

#transform string into number
int('1')
float('1.1')

#functions
1. def my_func(first_arg):
       return first_arg

2. def my_func(first_arg='Default value'):
       return first_arg

3. def my_func(first_arg, second_arg):
       return [first_arg, second_arg]
   my_func(second_arg=1, first_arg=2);

#loops
1. for: (go through elements in the iterable list)
       for block in block_list:
              print(block)
2. while: (execute code while condition is truthy)
       while a == b:
              print('Hello')