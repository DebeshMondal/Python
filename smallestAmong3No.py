# WRITE A PYTHON PROGRAM TO FIND THE SMALLER NO. BTW THREE NO.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c
print("The smallest number is:", smallest)

