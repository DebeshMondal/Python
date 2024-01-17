##a = int(input("Rows= "))
##b = int(input("Coloumns= "))
##
##i=0
##
##while i<a:
##    j=0
##    while j<b:
##        print('*' ,end=' ')
##        j+=1
##    print()
##    i+=1


a = int(input("Sides= "))

i=0

while i<a:
    j=0
    while(j<a):
        if i==j or i+j==(a-1):
            print('@ ',end='')
        else:
            print('* ',end='')
        j+=1
    print()
    i+=1
