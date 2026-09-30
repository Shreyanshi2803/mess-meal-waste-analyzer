from models import MealRecord
from validator import VALID_MEAL_TYPES, validate_record_values


def prompt_record(input_function=input):
    print("\nEnter meal record details")
    while True:
        date = input_function("Date (YYYY-MM-DD): ").strip()
        meal_type = input_function("Meal type (Breakfast/Lunch/Dinner): ").strip().capitalize()
        food_item = input_function("Food item: ").strip()
        prepared = input_function("Quantity prepared (kg): ").strip()
        consumed = input_function("Quantity consumed (kg): ").strip()
        valid, message = validate_record_values(date, meal_type, food_item, prepared, consumed)
        if valid:
            return MealRecord(date, meal_type, food_item, float(prepared), float(consumed))
        print(f"Invalid record: {message}")
        print(f"Valid meal types: {', '.join(VALID_MEAL_TYPES)}")
