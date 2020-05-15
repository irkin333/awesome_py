blockchain = [['0']]

def add_value(value):
    if(blockchain[-1]):
        blockchain.append([blockchain[-1], value])
    else:
        blockchain.append(value)
    print(blockchain)

add_value('a1')
add_value('b2')
add_value('c3')
    