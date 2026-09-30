from dataclasses import dataclass


@dataclass
class MealRecord:
    date: str
    meal_type: str
    food_item: str
    prepared_kg: float
    consumed_kg: float

    @property
    def waste_kg(self):
        return self.prepared_kg - self.consumed_kg
