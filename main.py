def get_user_input() -> list[int]:
    inputs = []

    print("Please enter your height in feet and inches as integers.")
    while True:
        try:
            feet = int(input("Feet: "))
            inputs.append(feet)
            break
        except ValueError:
            print("Input is not an integer. Please try again.")

    while True:
        try:
            inches = int(input("Inches: "))
            inputs.append(inches)
            break
        except ValueError:
            print("Input is not an integer. Please try again.")

    while True:
        try:
            weight = int(input("\nPlease enter your weight in pounds(lbs): "))
            inputs.append(weight)
            break
        except ValueError:
            print("Input is not an integer. Please try again.")

    return inputs


def calculateTotalInches(feet: int, inches: int) -> int:
    if feet < 0 or inches < 0:
        raise ValueError("Feet and inches must be non-negative integers.")
    return (feet * 12) + inches


class BMICalculator:
    def calculate_bmi(self, height: int, weight: int) -> float:
        # Multiply the weight in pounds by 0.45 (the metric conversion factor)
        weight = weight * 0.45

        # Multiply the height in inches by 0.025 (the metric conversion factor)
        height = height * 0.025

        # Square the height
        height = height**2

        # Divide the weight by the height. Round to nearest tenths place.
        return round(weight / height, 1)

    def categorize_bmi(self, bmi: float) -> str:
        if bmi < 18.5:
            return "Underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            return "Normal weight"
        elif bmi >= 25 and bmi <= 29.9:
            return "Overweight"
        elif bmi >= 30:
            return "Obese"


def main():
    # Get height(feet and inches) and weight from user
    # user_inputs[0] = feet
    # user_inputs[1] = inches
    # user_inputs[2] = weight(lbs)
    print("BMI Calculator\n")
    user_inputs = get_user_input()

    # Calculate user's height from feet and inches to just inches
    height = calculateTotalInches(user_inputs[0], user_inputs[1])

    # Calculate user's BMI
    bmi_calculator = BMICalculator()
    weight = user_inputs[2]
    bmi = bmi_calculator.calculate_bmi(height, weight)

    # Determine user's BMI category
    bmi_category = bmi_calculator.categorize_bmi(bmi)

    # Display user's BMI and BMI category
    print(f"\nYour BMI: {bmi}")
    print(f"Your BMI Category: {bmi_category}")


if __name__ == "__main__":
    main()
