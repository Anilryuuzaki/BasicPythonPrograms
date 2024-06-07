# Amstrong number

n = int(input('Enter the number: '))

amstrong = 0

for i in str(n): 
    amstrong+= int(i)**3
    
if (amstrong==n):
    print('The {} i a amstrong number'.format(n))
else:
    print('The {} is not a amstrong number'.format(n))    
