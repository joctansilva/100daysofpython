number_to_check = int(input("What is the number you want to check? "))
checked_number = number_to_check % 2
if checked_number == 0:
    print("The number is even")
else:
    print("The number is odd")
