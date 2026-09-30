import csv
from pathlib import Path

from models import MealRecord
from validator import validate_record_values

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
DATA_FILE = DATA_DIR / "meal_data.csv"
FIELDNAMES = ["date", "meal_type", "food_item", "prepared_kg", "consumed_kg"]


def load_records(file_path=DATA_FILE):
    path = Path(file_path)
    if not path.exists() or path.stat().st_size == 0:
        return []
    records = []
    try:
        with path.open("r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    values = (row["date"], row["meal_type"], row["food_item"],
                              row["prepared_kg"], row["consumed_kg"])
                    valid, _ = validate_record_values(*values)
                    if valid:
                        records.append(MealRecord(values[0].strip(), values[1].strip().capitalize(),
                                                  values[2].strip(), float(values[3]), float(values[4])))
                except (KeyError, TypeError, ValueError):
                    continue
    except OSError:
        return []
    return records


def save_record(record, file_path=DATA_FILE):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    needs_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        if needs_header:
            writer.writeheader()
        writer.writerow({"date": record.date, "meal_type": record.meal_type,
                         "food_item": record.food_item, "prepared_kg": f"{record.prepared_kg:.2f}",
                         "consumed_kg": f"{record.consumed_kg:.2f}"})
