def print_hi(name):
    var = input("Enter number: ")
    if var.isdecimal():
        re_var = reversed(var)

        if var == ''.join(re_var):
            print(var, ' is a pallendrone')
        else:
            print(var, ' is not a pallendrone')
    else:
        print(var, ' is not a number')


if __name__ == '__main__':
    print_hi('Solomon S A')

# See PyCharm help at https://www.jetbrain
