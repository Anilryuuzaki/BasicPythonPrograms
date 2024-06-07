# Reordering Sentence Words Based on Embedded Numerical Indicators
# Note: We are using a maximum of 0-9 numbers only for 1 sentence
#sentence = list(map(input().split())) are2 maximu5m o6f we1 num7bers sente11nce onl8y us3ing a4 fo9r o10ne  


'''def sort_sentence(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=lambda word: [char for char in word if char.isdigit()])
    sorted_sentence = ' '.join([word for word in sorted_words])
    return ''.join([i for i in sorted_sentence if not i.isdigit()])

# Test the function
sentence = "t2o j3oin 4WonderBiz I0 Technolog5ies wan1t"
print(sort_sentence(sentence))'''

from collections import defaultdict
m=defaultdict(str)
s=list(map(str,input().split(" ")))
for i in s:
    s1=""
    s2=""
    for j in i:
        if '0' <= j <= '12':
            s1 += j
        else:
            s2 += j
    m[int(s1)] = s2
for i in sorted(m.keys()):
    print(m[i], end=" ")


