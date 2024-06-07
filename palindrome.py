# palindrome: 
# reverse a string
word = input('Enter the word: ')
#reversing the string by using slicing method 
reverse = word[::-1]

if (reverse == word):
    print('The {} is a palindrome'.format(word))
else:
    print('The {} is not a palindrome'.format(word))

