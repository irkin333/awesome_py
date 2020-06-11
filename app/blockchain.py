blockchain = []
open_transactions = []
owner = 'Irina'


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    pass


def get_transaction_data():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = input('Your transaction amount, please: ')
    return (tx_recipient, tx_amount)


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
        tx_data = get_transaction_data()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
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

