'''
PRINT HOLLOW SQUARE USING *

'''

n=int(input("Enter no. of rows"))
i=1
while(i<=n):
    j=1
    while(j<=n):
        if(i==1 or i==n or j==1 or j==n ):
            print("*",end=' ')
        elif(i==j or (i+j)==(n+1)):
             print("@",end=' ')
        else:
            print(' ',end=' ')
            
        j+=1
    i+=1
    print()
        