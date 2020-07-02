genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Irina'


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def mine_block():
    global open_transactions
    hashed_block = hash_block(blockchain[-1])

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    open_transactions = []


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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('Please, choose:')
    print('1: Add a new value to the blockchain')
    print('2: Mine a new block')
    print('3: Output all the block in blockchain')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_data()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Irina', 'amount': 1}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        loop = False
        print('Input was invalid, please, pick value from the list!')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain.')
        break

