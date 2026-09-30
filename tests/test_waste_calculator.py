import unittest

from waste_calculator import (calculate_waste, calculate_waste_percentage,
                              classify_waste)


class WasteCalculatorTests(unittest.TestCase):
    def test_waste_quantity(self):
        self.assertEqual(calculate_waste(10, 7), 3)

    def test_waste_percentage(self):
        self.assertAlmostEqual(calculate_waste_percentage(10, 7), 30)

    def test_zero_prepared_percentage(self):
        self.assertEqual(calculate_waste_percentage(0, 0), 0)

    def test_classification(self):
        self.assertEqual(classify_waste(5), "LOW")
        self.assertEqual(classify_waste(15), "MODERATE")
        self.assertEqual(classify_waste(30), "HIGH")
        self.assertEqual(classify_waste(50), "CRITICAL")
