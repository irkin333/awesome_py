blockchain = []

def get_last_blockchain_value():
    """ Retuns last value from blockchain list """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value():
    value = input('Value for the blockchain: ')
    last_blockchain_value = get_last_blockchain_value()
    if last_blockchain_value:
        blockchain.append([get_last_blockchain_value(), value])
    else:
        blockchain.append([value])


def print_blockchain_elements():
    for block in blockchain:
        print(block)


def get_user_choice():
    return input('Your choice is: ')

def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] != blockchain[block_index - 1]:
            is_valid = False
            break
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please, choose:')
    print('1: Add a new value to the blockchain')
    print('2: Output all the block in blockchain')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        add_value()
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        loop = False
        print('Input was invalid, please, pick value from the list!')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain.')
        break

