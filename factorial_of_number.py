#find the factorial of a number
n = int(input('Enter the number: '))

if (n<0):
    print('{} is a invalid number'.format(n))
elif (n==0):
    print('The factorial of {} is 1'.format(n))  
else: 
    factorial = 1     
    for i in range(1, n+1):
        factorial*= i
    print('The factorial of {} is {}'.format(n, factorial))