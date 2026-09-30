import unittest

from analyzer import analyze_records
from models import MealRecord


class AnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            MealRecord("2026-09-01", "Lunch", "Rice", 20, 10),
            MealRecord("2026-09-01", "Dinner", "Dal", 10, 9),
            MealRecord("2026-09-02", "Dinner", "Rice", 12, 6),
        ]

    def test_totals_and_highest_food(self):
        result = analyze_records(self.records)
        self.assertEqual(result["total_waste"], 17)
        self.assertEqual(result["highest_waste_food"], "Rice")

    def test_meal_analysis(self):
        result = analyze_records(self.records)
        self.assertEqual(result["highest_waste_meal"], "Lunch")
        self.assertEqual(result["high_waste_count"], 2)

    def test_empty_analysis(self):
        result = analyze_records([])
        self.assertEqual(result["record_count"], 0)
        self.assertEqual(result["overall_percentage"], 0.0)
        self.assertEqual(result["highest_waste_food"], "None")
