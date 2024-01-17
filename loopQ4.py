#PRINT ALL ODD NO. FROM N1 TO N2.



n1 = int(input("Enter the value of n1: "))
n2 = int(input("Enter the value of n2: "))
i = n1
while i <= n2:
    if i % 2 != 0:
        print(i)
    i += 1
