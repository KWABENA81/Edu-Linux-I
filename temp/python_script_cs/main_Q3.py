def print_hi(name):
    first = 1000
    last = 3000
    for x in range(first, last + 1):
        var = x
        if var % 2 == 0:
            var = int(x / 10)
            if var % 2 == 0:
                var = int(x / 100)
                if var % 2 == 0:
                    var = int(x / 1000)
                    if var % 2 == 0:
                        print(x)


if __name__ == '__main__':
    print_hi('Solomon S A')

# See PyCharm help at https://www.jetbrain
