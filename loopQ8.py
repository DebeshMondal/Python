#print all no. divisible by 4 but not by 6 within a range

a=int(input('First no.= '))
b=int(input('Second no. '))

while (a<=b):
    if a%4 == 0 and a%6 != 0:
        print(a)
    a+=1
 
