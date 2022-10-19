sentence = input("Enter comma-separated words: ")
word_list = sentence.split(',')
sorted_words = sorted(word_list)

w_list = ''
for w in sorted_words:
    if len(w_list) != 0:
        w_list += ','
    w_list += w

print(w_list)


# Enter comma-separated words: without,hello,bag,world
# bag,hello,without,world
