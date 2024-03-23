def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    weight = float(input("Enter weight (in kg): "))
    height = float(input("Enter height (in meters): "))
    bmi = calculate_bmi(weight, height)
    print("BMI:", bmi)

if __name__ == "__main__":
    main()
