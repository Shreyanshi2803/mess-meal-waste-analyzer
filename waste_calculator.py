LOW_LIMIT = 10.0
MODERATE_LIMIT = 25.0
HIGH_LIMIT = 40.0


def calculate_waste(prepared_kg, consumed_kg):
    return max(0.0, float(prepared_kg) - float(consumed_kg))


def calculate_waste_percentage(prepared_kg, consumed_kg):
    prepared = float(prepared_kg)
    if prepared == 0:
        return 0.0
    return calculate_waste(prepared, consumed_kg) / prepared * 100


def classify_waste(waste_percentage, low_limit=LOW_LIMIT,
                   moderate_limit=MODERATE_LIMIT, high_limit=HIGH_LIMIT):
    percentage = float(waste_percentage)
    if percentage <= low_limit:
        return "LOW"
    if percentage <= moderate_limit:
        return "MODERATE"
    if percentage <= high_limit:
        return "HIGH"
    return "CRITICAL"
