def calculate_BMI(weight, height):
    BMI = weight / height ** 2
    return BMI


def interpret_BMI(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25:
        return "Correct weight"
    elif 25 <= BMI < 29.9:
        return "Overweight"
    elif 29.9 <= BMI:
        return "Obesity"


weight = float(input("Enter the weight (in kilograms): "))
height = float(input("Enter the height (in meters): "))

result_BMI = calculate_BMI(weight, height)
interpretation = interpret_BMI(result_BMI)

print("Your BMI is:", result_BMI)
print("interpretation BMI:", interpretation)
