#PRINT ALL THE NUMBERS DIVISIBLE BY 4 AND 6 BTW TWO GIVEN RANGES USING WHILE LOOP

# Get user input for the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Ensure that the end_range is greater than or equal to start_range
while end_range < start_range:
    print("Invalid input. End of the range should be greater than or equal to the start of the range.")
    end_range = int(input("Enter the end of the range: "))

# Initialize a variable for the current number
current_number = start_range

# Iterate through the numbers in the specified range
while current_number <= end_range:
    # Check if the current number is divisible by both 4 and 6
    if current_number % 4 == 0 and current_number % 6 == 0:
    #if current_number % 4 == 0 or current_number % 6 == 0:
        print(current_number)
    
    # Move to the next number
    current_number += 1
