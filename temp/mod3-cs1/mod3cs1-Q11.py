def read_lines():
    print('Enter multi-line input: Ctrl-D or Ctrl-Z to proceed')
    mlines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        mlines.append(line)

    para = '\n'.join(mlines)
    return para.upper()


print(read_lines())


# Hello world
# Practice makes perfect
# ^D
# HELLO WORLD
# PRACTICE MAKES PERFECT