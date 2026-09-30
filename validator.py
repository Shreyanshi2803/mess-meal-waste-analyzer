from datetime import datetime

VALID_MEAL_TYPES = ("Breakfast", "Lunch", "Dinner")


def validate_date(value):
    try:
        datetime.strptime(value.strip(), "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


def validate_meal_type(value):
    if not isinstance(value, str):
        return False
    return value.strip().capitalize() in VALID_MEAL_TYPES


def validate_food_name(value):
    return isinstance(value, str) and bool(value.strip())


def validate_quantity(value):
    try:
        return float(value) >= 0
    except (TypeError, ValueError):
        return False


def validate_record_values(date, meal_type, food_item, prepared_kg, consumed_kg):
    if not validate_date(date):
        return False, "Date must use YYYY-MM-DD format."
    if not validate_meal_type(meal_type):
        return False, "Meal type must be Breakfast, Lunch, or Dinner."
    if not validate_food_name(food_item):
        return False, "Food name cannot be empty."
    if not validate_quantity(prepared_kg) or not validate_quantity(consumed_kg):
        return False, "Quantities must be non-negative numbers."
    if float(consumed_kg) > float(prepared_kg):
        return False, "Consumed quantity cannot exceed prepared quantity."
    return True, ""
