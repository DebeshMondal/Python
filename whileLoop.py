'''
A B C D
A B C D
A B C D
A B C D
A B C D

n= int(input("Enter no. of rows"))
i=0
p=65
while i<n:
     j=0
     while j<n:
         print(chr(65+j),end=' ')
         j+=1
         p+=1
     i+=1
     print()

'''

'''
n=int(input("Enter the no. of rows"))
i=1
j=0
while(i<=n):
    j=0
    while(j<i):
        print('*',end=' ')
        j+=1
    i+=1
    print('')


'''



'''
n=int(input("Enter the no. of rows"))
i=n
while(i>0):
    j=0
    while(j<i):
        print('*',end=' ')
        j+=1
    print('')
    i-=1
    
'''



'''
n=int(input("Enter the no. of rows"))
i=1
j=1
k=1
while(i<=n):
    j=1
    k=1
    while(j<=n-i):
        print(' ',end=' ')
        j+=1
    while(k<=i):
        print('*',end=' ')
        k+=1
    print('')
    i+=1

'''


n=int(input("Enter the no. of rows"))
i=1
j=1
k=1
while(i<=n):
    j=1
    k=1
    while(k<i):
        print(' ',end=' ')
        k+=1
    while(j<=n-i+1):
        print('*',end=' ')
        j+=1
    
    print('')
    i+=1


