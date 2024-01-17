#print all the factors of a given number

n=int(input("Enter any no. "))
a=1
while a<=n:
    if n%a==0 :
        print(a)
a=a+1
