def print_hi(name):
    var = input("enter word sequence:")

    digits = 0
    letters = 0
    for i, x in enumerate(var):
        if x.isdigit():
            digits = digits + 1
        if x.isalpha():
            letters = letters + 1

    print('LETTERS: ', letters)
    print('DIGITS: ', digits)


if __name__ == '__main__':
    print_hi('Solomon S A')

# See PyCharm help at https://www.jetbrain
