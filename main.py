from sys import exit


def get_user_input() -> list[int]:
    inputs = []

    print("Please enter your height in feet and inches as integers.")
    while True:
        try:
            feet = int(input("Feet: "))

            if feet < 0:
                raise ValueError("Feet can't be a negative integer.")
            else:
                inputs.append(feet)
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid, non-negative integer.")

    while True:
        try:
            inches = int(input("Inches: "))

            if inches < 0:
                raise ValueError("Inches can't be a negative integer.")
            else:
                inputs.append(inches)
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid, non-negative integer.")

    while True:
        try:
            weight = int(input("\nPlease enter your weight in pounds(lbs): "))

            if weight < 0:
                raise ValueError("Weight can't be a negative integer.")
            else:
                inputs.append(weight)
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid, non-negative integer.")

    return inputs


def calculate_total_inches(feet: int, inches: int) -> int:
    if feet < 0 or inches < 0:
        raise ValueError("Feet and inches must be non-negative integers.")
    return (feet * 12) + inches


class BMICalculator:
    def calculate_bmi(self, height: int, weight: int) -> float:
        if height < 0 or weight < 0:
            raise ValueError("Height and weight must be non-negative integers.")

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
    bmi_calculator = BMICalculator()

    while True:
        # Display menu options
        print("=" * 20)
        print(
            "1. get_user_input - This function asks the user to enter 3 integers for height(feet and inches) and weight."
        )
        print(
            "2. calculate_total_inches - This function converts feet and inches to just inches."
        )
        print(
            "3. calculate_bmi - This is a method of the BMICalculator class that calculates your BMI based on your height(inches) and weight(lbs)."
        )
        print(
            "4. categorize_bmi - This is a method of the BMICalculator class that returns a category string based on your BMI."
        )
        print("5. Exit Program.")
        print("=" * 20)

        option = None
        try:
            option = int(input("Select which option to run: "))
            if option < 1 or option > 5:
                raise ValueError("Invalid option choice. Enter an integer between 1-5.")
        except ValueError as e:
            print(
                f"Invalid input: {e}. Please enter a valid, non-negative integer between 1-5."
            )
            continue

        if option == 1:
            output = get_user_input()
            print("Displaying output of function")
            print(f"Feet: {output[0]}")
            print(f"Inches: {output[1]}")
            print(f"Weight(lbs): {output[2]}\n")
        elif option == 2:
            print("Please enter your height in feet and inches as integers.")
            inputs = []

            while True:
                try:
                    feet = int(input("Feet: "))

                    if feet < 0:
                        raise ValueError("Feet can't be a negative integer.")
                    else:
                        inputs.append(feet)
                    break
                except ValueError as e:
                    print(
                        f"Invalid input: {e}. Please enter a valid, non-negative integer."
                    )

            while True:
                try:
                    inches = int(input("Inches: "))

                    if inches < 0:
                        raise ValueError("Inches can't be a negative integer.")
                    else:
                        inputs.append(inches)
                    break
                except ValueError as e:
                    print(
                        f"Invalid input: {e}. Please enter a valid, non-negative integer."
                    )

            output = calculate_total_inches(inputs[0], inputs[1])
            print(f"{inputs[0]}'{inputs[1]} is equal to {output} inches\n")
        elif option == 3:
            inputs = get_user_input()
            height = calculate_total_inches(inputs[0], inputs[1])
            weight = inputs[2]

            bmi = bmi_calculator.calculate_bmi(height, weight)
            print(f"Your BMI: {bmi}\n")
        elif option == 4:
            bmi = None
            while True:
                try:
                    bmi = round(float(input("Enter your bmi: ")), 1)

                    if bmi < 0.0:
                        raise ValueError("Inches can't be a negative integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a non-negative bmi.")

            bmi_category = bmi_calculator.categorize_bmi(bmi)
            print(f"Your BMI Category: {bmi_category}\n")
        elif option == 5:
            exit()


if __name__ == "__main__":
    main()
