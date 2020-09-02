import functools

MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Irina'
participants = { 'Max' }


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + int(tx_amt[0]) if len(tx_amt) > 0 else 0, tx_sender, 0)

    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + int(tx_amt[0]) if len(tx_amt) > 0 else 0, tx_recipient, 0)

    return amount_received - amount_sent


def verify_transaction(tx):
    sender_balance = get_balance(tx['sender'])
    return sender_balance >= int(tx['amount'])


def mine_block():
    hashed_block = hash_block(blockchain[-1])
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    return True


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


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print('Please, choose:')
    print('1: Add a new value to the blockchain')
    print('2: Mine a new block')
    print('3: Output all the block in blockchain')
    print('4: Output participants of the blockchain')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_data()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Transaction was successful!')
        else: 
            print('Transaction failed! Not enough funds')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block(): 
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        print(verify_transactions())
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
        print('Invalid blockchain. Balance of {}: {}'.format('Iryna', get_balance('Iryna')))
        break

    print(get_balance('Irina'))

