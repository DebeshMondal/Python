#PRINT E USING SEVEN SEGMENT
'''
****
*
***
*
****




n=int(input("Enter no. of rows"))
i=1
while(i<=n):
    j=1
    while(j<=n):
        if(i==1  or j==1 or i==n or i==3):
            print("*",end=' ')
        else:
            print(' ',end=' ')
            
        j+=1
    i+=1
    print()


'''



n= int(input("Enter no. of rows"))
i=1
p=65
while(i<=n):
    j=1
    while(j<=n):
         print(chr (p),end=' ')
         j+=1
    i+=1
    p+=1
    print()



