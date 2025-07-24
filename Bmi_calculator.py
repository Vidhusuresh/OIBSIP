#for weight calculation
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
#for categorization
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

print("Welcome to the BMI Calculator")
try:
       
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    if weight <= 0 or height <= 0:
        print("Height and weight must be positive numbers.")
            

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {category}")

except ValueError:
    print("Please enter valid numeric input.")
