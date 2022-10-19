sentence = 'hello world and practice makes perfect and hello world again'
word_list = sentence.split()
word_list.sort(reverse=False)
print(word_list)
unique_word_list = []
for w in word_list:
    if w not in unique_word_list:
        unique_word_list.append(w)

print(*unique_word_list)




# ['again', 'and', 'and', 'hello', 'hello', 'makes', 'perfect', 'practice', 'world', 'world']
# again and hello makes perfect practice world