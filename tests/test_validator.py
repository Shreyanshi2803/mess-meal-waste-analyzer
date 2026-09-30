import unittest

from validator import (validate_date, validate_food_name, validate_meal_type,
                       validate_record_values, validate_quantity)


class ValidatorTests(unittest.TestCase):
    def test_valid_values(self):
        self.assertTrue(validate_date("2026-09-27"))
        self.assertTrue(validate_meal_type("Dinner"))
        self.assertTrue(validate_food_name("Rice"))
        self.assertTrue(validate_quantity("2.5"))

    def test_invalid_values(self):
        self.assertFalse(validate_date("27/09/2026"))
        self.assertFalse(validate_meal_type("Snack"))
        self.assertFalse(validate_food_name("  "))
        self.assertFalse(validate_quantity("-1"))
        valid, _ = validate_record_values("2026-09-27", "Lunch", "Rice", 2, 3)
        self.assertFalse(valid)
