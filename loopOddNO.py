#PRINT ALL ODD NO. FROM 1 TO N.


n = int(input("Enter the value of n: "))
i = 1
while i <= n:
    if i % 2 == 1:
        print(i)
    i += 2

