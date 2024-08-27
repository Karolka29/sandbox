number = int(input("Enter an integer: "))
if number % 3 == 0 and number % 5 == 0:
    print("The entered value is divisible by 3 and by 5.")
elif number % 3 == 0 and number % 5 != 0:
    print("The entered value is divisible by 3 but not by 5.")
elif number % 3 != 0 and number % 5 == 0:
    print("The entered value is divisible by 5 but not by 3.")
else:
    print("The entered value is not divisible by either 3 or 5.")