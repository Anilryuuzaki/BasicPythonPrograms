#print sum of n numbers program

#Taking n value from the user
n = int(input("Enter the value of n: "))
sum = 0
#
for i in range(n+1) :
    sum = sum + i

print("The sum of n is ",sum)

