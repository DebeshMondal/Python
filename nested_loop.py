###Nested while loop
###--------------------------
###Orange Mango Mango Mango
###Orange Mango Mango Mango
###Orange Mango Mango Mango
##
###use one print for Orange
###and 
###use one print for Mango
##
##
### Define the number of rows and columns
##rows = 3
##columns = 4
##
### Initialize variables for Orange and Mango
##orange = "Orange"
##mango = "Mango"
##
### Outer loop for rows
##row = 1
##while row <= rows:
##    # Print Orange once in a row
##    print(orange, end=" ")
##
##    # Inner loop for columns
##    col = 1
##    while col < columns:
##        # Print Mango multiple times in a row
##        print(mango, end=" ")
##        col += 1
##    
##    # Move to the next row
##    print()  # Move to the next line after printing a row
##    row += 1
##

a = "Orange"
b = "Mango"

i = 1

while i <= 3:
    j = 1
    print(a, " ", end="")
    i += 1
    while j <= 3:
        print(b, " ", end="")
        j += 1
    print(" ")  # Correct indentation for this line


















