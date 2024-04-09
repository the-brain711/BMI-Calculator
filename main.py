from sys import exit, argv
import streamlit


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
        if height <= 0 or weight <= 0:
            raise ValueError(
                "Height and weight must be non-zero and non-negative integers."
            )

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


def console_mode():
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
                    bmi = float(input("Enter your bmi: "))

                    if bmi < 0.0:
                        raise ValueError("Inches can't be a negative integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a non-negative bmi.")

            bmi_category = bmi_calculator.categorize_bmi(bmi)
            print(f"Your BMI Category: {bmi_category}\n")
        elif option == 5:
            exit()


def web_app_mode():
    bmi_calculator = BMICalculator()

    def check_input(x, msg, check_for_zero=False):
        try:
            if check_for_zero:
                if x <= 0:
                    raise ValueError(msg)
            else:
                if x < 0:
                    raise ValueError(msg)
        except ValueError as e:
            streamlit.exception(e)

    # Title of web app
    streamlit.markdown("# BMI Calculator")

    # Ask for feet and inches for height
    streamlit.markdown("### Height")
    feet = streamlit.number_input("Feet", step=1)
    inches = streamlit.number_input("Inches", step=1)
    total_height = 0
    height_textbox = streamlit.empty()
    height_text = height_textbox.text(f"Total Height in Inches: {total_height}")

    if streamlit.button("Convert Height to Inches"):
        check_input(feet, "Feet can't be a negative integer.")
        check_input(inches, "Inches can't be a negative integer.")
        total_height = calculate_total_inches(feet, inches)
        height_text = height_textbox.text(f"Total Height in Inches: {total_height}")

    # Ask for weight in lbs
    streamlit.markdown("### Weight")
    weight = streamlit.number_input("Weight in lbs", step=1)

    # BMI
    streamlit.markdown("### BMI")
    bmi = 0
    bmi_textbox = streamlit.empty()
    bmi_text = bmi_textbox.text(f"BMI: {bmi}")
    if streamlit.button("Calculate BMI"):
        total_height = calculate_total_inches(feet, inches)
        check_input(
            total_height, "Total Height must be a non-zero, non-negative integer."
        )
        check_input(weight, "Weight must be a non-zero, non-negative integer.")
        bmi = bmi_calculator.calculate_bmi(total_height, weight)
        bmi_text = bmi_textbox.text(f"BMI: {bmi}")

    bmi_category = "None"
    bmi_category_textbox = streamlit.empty()
    bmi_category_text = bmi_category_textbox.text(f"BMI Category: {bmi_category}")
    if streamlit.button("Categorize BMI"):
        total_height = calculate_total_inches(feet, inches)
        check_input(
            total_height, "Total Height must be a non-zero, non-negative integer."
        )
        check_input(weight, "Weight must be a non-zero, non-negative integer.")
        bmi = bmi_calculator.calculate_bmi(total_height, weight)
        bmi_category = bmi_calculator.categorize_bmi(bmi)
        bmi_category_text = bmi_category_textbox.text(f"BMI Category: {bmi_category}")


if __name__ == "__main__":
    if len(argv) == 2 and argv[1] == "-console":
        console_mode()
    else:
        web_app_mode()
