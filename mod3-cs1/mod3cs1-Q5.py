def read_input():
    menu = 'Select from the options:\n'
    menu += 'Cash Withdrawal (W or w)\n'
    menu += 'Cash Credit (C or c)\n'
    menu += 'Change Password (P or p)\n'
    menu += 'EXIT (X or x)\n'
    menu += '#: '
    return input(menu)


user_input = ''
while True:
    try:
        user_input = read_input().upper()
    except EOFError:
        break
    if user_input == 'W':
        print('\t\tSelected Cash Withdrawal\n')
    elif user_input == 'C':
        print('\t\tSelected Cash Credit\n')
    elif user_input == 'P':
        print('\t\tSelected Change Password\n')
    elif user_input == 'X':
        print('\t\tThanks for your patronage\n')
        break
    else:
        print('\t\tinvalid selection\n\n')
        continue
