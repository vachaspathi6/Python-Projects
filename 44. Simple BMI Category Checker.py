def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight = float(input("Enter weight (in kg): "))
    height = float(input("Enter height (in meters): "))
    bmi = calculate_bmi(weight, height)
    print("BMI:", bmi)
    print("BMI Category:", bmi_category(bmi))

if __name__ == "__main__":
    main()
