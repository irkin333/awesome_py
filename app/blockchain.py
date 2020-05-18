blockchain = [['0']]


def get_last_blockchain_value():
    """ Retuns last value from blockchain list """
    return blockchain[-1]


def add_value(value):
    if(blockchain[-1]):
        blockchain.append([get_last_blockchain_value(),
                           value])
    else:
        blockchain.append(value)
    print(blockchain)


add_value('a1')
add_value('b2')
add_value('c3')
