def print_hi(name):
    var = 155
    print('This is ', name)
    if var > 1:
        for n in range(2, var):
            if n > var / 2:
                break
            if var % n == 0:
                print(n, ' is a factor of', var)
                if n % 2 == 0 or n == var:
                    print(n, ' is even ')
                else:
                    print(n, ' is odd ')
        print(var, ' is a factor of itself')
    else:
        print('factor of ', var, 'is undefined')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Solomon S A')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
