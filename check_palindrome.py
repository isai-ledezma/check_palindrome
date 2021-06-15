def reverser(splited_text):
    c = 1
    text_leng = len(splited_text)
    for label in splited_text:
        reverse_text.append(splited_text[text_leng-c])
        c += 1
    return reverse_text


word = input('give me the word or words')
reverse_text = []
splited_text = []
for c in word:
    splited_text.append(c)

reverser(splited_text)

if splited_text == reverse_text:
    print('is a palindrome!')
else:
    print('is not a palindrome')
print('text:')
print(word)
print('reverse:')
print(reverse_text)



