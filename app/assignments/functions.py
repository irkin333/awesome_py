# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

def normal_func(*args):
    for (i, arg) in enumerate(args):
        if i == 0: 
            continue
        result = args[0](arg)
        print(result)


def test_func(arg):
    return arg

normal_func(test_func, 'argument one', 'argument two')

# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
normal_func(lambda arg: arg, 'lambda arg 1', 'lambda arg 2', 'lambda arg 3')
