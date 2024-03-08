import unittest
from main import *


class TestBMICalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.bmi_calculator = BMICalculator()

    def test_calculate_bmi(self):
        result = self.bmi_calculator.calculate_bmi(63, 125)
        msg = f"test_calculate_bmi unit test failed. {result} does not equal 22.7."
        self.assertEqual(22.7, result, msg)

        # Raise error is inputs are negative integers
        self.assertRaises(ValueError, self.bmi_calculator.calculate_bmi, -1, 100)
        self.assertRaises(ValueError, self.bmi_calculator.calculate_bmi, 60, -1)
        self.assertRaises(ValueError, self.bmi_calculator.calculate_bmi, -1, -1)

    def test_categorize_bmi(self):
        # Test Underweight Category
        current = 0
        while current < 18.5:
            result = self.bmi_calculator.categorize_bmi(current)
            msg = f"test_categorize_bmi unit test failed. {result} does not equal Underweight."
            self.assertEqual("Underweight", result, msg)
            current += 0.1

        # Test Normal Weight Category
        current = 18.5
        while current <= 24.9:
            result = self.bmi_calculator.categorize_bmi(current)
            msg = f"test_categorize_bmi unit test failed. {result} does not equal Normal weight."
            self.assertEqual("Normal weight", result, msg)
            current += 0.1

        # Test Overweight Category
        current = 25
        while current <= 29.9:
            result = self.bmi_calculator.categorize_bmi(current)
            msg = f"test_categorize_bmi unit test failed. {result} does not equal Overweight."
            self.assertEqual("Overweight", result, msg)
            current += 0.1

        # Test Obese Category
        current = 30
        while current >= 30:
            result = self.bmi_calculator.categorize_bmi(current)
            msg = f"test_categorize_bmi unit test failed. {result} does not equal Overweight."
            self.assertEqual("Overweight", result, msg)
            current += 0.1

            if current == 31.1:
                break
