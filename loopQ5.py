#print factorial of a given number in python

N= int(input('Enter the no. '))

i = 1
fact = 1
while (i <= N):
    fact = fact*i
    i+=1
print(fact)    
