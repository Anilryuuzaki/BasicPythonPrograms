# reverse a string
word = input('Enter the word to reverse: ')
reverse = ""
for i in word:
    reverse = i + reverse

print('The reversed word is {}'.format(reverse))