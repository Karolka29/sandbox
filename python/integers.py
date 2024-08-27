def enter_a_nonnegative_integer():
    while True:
        try:
            number = int(input("Enter_a_nonnegative_integer: "))
            if number >= 0:
                return number
            else:
                print("The specified number must be non-negative, please try again.")
        except ValueError:
            print("This is not an integer, Please try again.")

a = enter_a_nonnegative_integer()
b = enter_a_nonnegative_integer()
c = enter_a_nonnegative_integer()

if a == b == c:
    print('All numbers are the same.')

else:
    largest_number = max(a, b, c)
    print("The largest number is:", largest_number)

