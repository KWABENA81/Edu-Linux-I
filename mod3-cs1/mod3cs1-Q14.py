
var = input("Enter string: ")
lcase = 0
ucase = 0
for i, x in enumerate(var):

    if 65 <= ord(x) <= 90:
        ucase += 1
    elif 97 <= ord(x) <= 122:
        lcase += 1

#   'A' = 65 , 'Z' = 90, 'a' = 97, 'z' = 122
print('UPPERCASE: ', ucase)
print('LOWERCASE: ', lcase)


# Enter string: Hello world!
# UPPERCASE:  1
# LOWERCASE:  9

# Enter string: Python is INtesting, But I AM still LEarning
# UPPERCASE:  9
# LOWERCASE:  27