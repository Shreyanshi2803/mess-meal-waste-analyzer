from collections import defaultdict
from datetime import datetime

from waste_calculator import (HIGH_LIMIT, calculate_waste_percentage,
                              classify_waste)


def _empty_stats():
    return {"prepared": 0.0, "consumed": 0.0, "waste": 0.0, "records": 0}


def _add_stat(stats, key, record):
    if key not in stats:
        stats[key] = _empty_stats()
    stats[key]["prepared"] += record.prepared_kg
    stats[key]["consumed"] += record.consumed_kg
    stats[key]["waste"] += record.waste_kg
    stats[key]["records"] += 1


def _with_percentages(stats):
    for values in stats.values():
        values["waste_percentage"] = (values["waste"] / values["prepared"] * 100
                                       if values["prepared"] else 0.0)
        values["average_waste"] = (values["waste"] / values["records"]
                                    if values["records"] else 0.0)
        values["status"] = classify_waste(values["waste_percentage"])
    return stats


def analyze_records(records):
    food_stats = {}
    meal_stats = {}
    day_stats = {}
    total_prepared = sum(record.prepared_kg for record in records)
    total_consumed = sum(record.consumed_kg for record in records)
    total_waste = sum(record.waste_kg for record in records)

    for record in records:
        _add_stat(food_stats, record.food_item, record)
        _add_stat(meal_stats, record.meal_type, record)
        _add_stat(day_stats, record.date, record)

    _with_percentages(food_stats)
    _with_percentages(meal_stats)
    _with_percentages(day_stats)
    overall_percentage = total_waste / total_prepared * 100 if total_prepared else 0.0
    average_daily_waste = total_waste / len(day_stats) if day_stats else 0.0
    high_records = [record for record in records
                    if classify_waste(calculate_waste_percentage(record.prepared_kg,
                                                                 record.consumed_kg)) in ("HIGH", "CRITICAL")]
    average_record_waste = total_waste / len(records) if records else 0.0
    unusual_records = [record for record in records
                       if record.waste_kg > average_record_waste * 1.5 and record.waste_kg > 0]
    high_waste_saving = sum(record.waste_kg * 0.5 for record in high_records)
    days = len(day_stats)

    return {
        "record_count": len(records), "total_prepared": total_prepared,
        "total_consumed": total_consumed, "total_waste": total_waste,
        "overall_percentage": overall_percentage,
        "overall_status": classify_waste(overall_percentage),
        "average_daily_waste": average_daily_waste,
        "food_stats": food_stats, "meal_stats": meal_stats, "day_stats": day_stats,
        "highest_waste_food": max(food_stats, key=lambda key: food_stats[key]["waste"], default="None"),
        "highest_waste_percentage_food": max(food_stats, key=lambda key: food_stats[key]["waste_percentage"], default="None"),
        "highest_waste_meal": max(meal_stats, key=lambda key: meal_stats[key]["average_waste"], default="None"),
        "highest_waste_day": max(day_stats, key=lambda key: day_stats[key]["waste"], default="None"),
        "lowest_waste_food": min(food_stats, key=lambda key: food_stats[key]["waste"], default="None"),
        "high_waste_records": high_records, "low_waste_count": sum(1 for record in records if classify_waste(calculate_waste_percentage(record.prepared_kg, record.consumed_kg)) == "LOW"),
        "high_waste_count": len(high_records), "problematic_foods": [key for key, value in food_stats.items() if value["status"] in ("HIGH", "CRITICAL")],
        "problematic_meals": [key for key, value in meal_stats.items() if value["status"] in ("HIGH", "CRITICAL")],
        "unusual_records": unusual_records, "estimated_weekly_saving": high_waste_saving * (7 / days) if days else 0.0,
    }
