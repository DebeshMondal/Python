science = int(input("Enter the marks in science: "))
math = int(input("Enter the marks in math: "))
english = int(input("Enter the marks in English: "))
hindi = int(input("Enter the marks in Hindi: "))

if science > 100 or math > 100 or english > 100 or hindi > 100:
    print("Enter valid numbers (marks should be between 0 and 100).")
else:
    average = (science + math + english + hindi) / 4

    if science < 40 or math < 40 or english < 40 or hindi < 40:
        print("The student has failed.")
    else:
        if average >= 80:
            print("The student is allotted to science.")
        elif 60 <= average < 80:
            print("The student is allotted to commerce.")
        elif 40 <= average < 60:
            print("The student is allotted to arts.")
        else:
            print("Invalid average marks.")
