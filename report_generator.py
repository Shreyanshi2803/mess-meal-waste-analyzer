from waste_calculator import calculate_waste_percentage


def _kg(value):
    return f"{value:.2f} kg"


def _print_stats(title, stats):
    print(f"\n--- {title} ---")
    if not stats:
        print("No data available.")
        return
    for key, values in sorted(stats.items()):
        print(f"{key}: waste {_kg(values['waste'])}, rate {values['waste_percentage']:.1f}%, "
              f"average {_kg(values['average_waste'])}, status {values['status']}")


def print_records(records):
    print("\n--- Entered Records ---")
    if not records:
        print("No records available.")
        return
    for index, record in enumerate(records, 1):
        percentage = calculate_waste_percentage(record.prepared_kg, record.consumed_kg)
        print(f"{index}. {record.date} | {record.meal_type} | {record.food_item} | "
              f"prepared {_kg(record.prepared_kg)} | consumed {_kg(record.consumed_kg)} | "
              f"waste {_kg(record.waste_kg)} ({percentage:.1f}%)")


def print_summary(analysis):
    print("\n--- Waste Analysis ---")
    if not analysis["record_count"]:
        print("No records available for analysis.")
        return
    print(f"Records analyzed: {analysis['record_count']}")
    print(f"Total prepared: {_kg(analysis['total_prepared'])}")
    print(f"Total consumed: {_kg(analysis['total_consumed'])}")
    print(f"Total wasted: {_kg(analysis['total_waste'])}")
    print(f"Overall waste rate: {analysis['overall_percentage']:.1f}% ({analysis['overall_status']})")
    print(f"Average daily waste: {_kg(analysis['average_daily_waste'])}")
    print(f"High-waste records: {analysis['high_waste_count']}")
    print(f"Low-waste records: {analysis['low_waste_count']}")
    print(f"Highest-waste food: {analysis['highest_waste_food']}")
    print(f"Highest-waste meal: {analysis['highest_waste_meal']}")
    print(f"Highest-waste day: {analysis['highest_waste_day']}")
    print(f"Lowest-waste food: {analysis['lowest_waste_food']}")


def print_high_waste(analysis):
    print("\n--- High-Waste Records ---")
    records = analysis["high_waste_records"]
    if not records:
        print("No high-waste records found.")
        return
    for record in records:
        percentage = calculate_waste_percentage(record.prepared_kg, record.consumed_kg)
        print(f"{record.date} | {record.meal_type} | {record.food_item} | "
              f"{_kg(record.waste_kg)} wasted ({percentage:.1f}%)")


def print_recommendations(analysis, recommendations):
    print("\n--- Recommendations ---")
    for number, recommendation in enumerate(recommendations, 1):
        print(f"{number}. {recommendation}")
    print(f"Estimated weekly saving: {_kg(analysis['estimated_weekly_saving'])}")


def print_intelligence_report(analysis, recommendations):
    print("\n" + "=" * 48)
    print("        MESS WASTE INTELLIGENCE REPORT")
    print("=" * 48)
    print(f"Total Prepared: {_kg(analysis['total_prepared'])}")
    print(f"Total Consumed: {_kg(analysis['total_consumed'])}")
    print(f"Total Wasted: {_kg(analysis['total_waste'])}")
    print(f"Overall Waste Rate: {analysis['overall_percentage']:.1f}%")
    print(f"Waste Status: {analysis['overall_status']}")
    if analysis["record_count"]:
        print(f"Highest Waste Food: {analysis['highest_waste_food']}")
        print(f"Highest Waste Meal: {analysis['highest_waste_meal']}")
        print(f"Highest Waste Day: {analysis['highest_waste_day']}")
        print("\nMain Findings:")
        print(f"- Highest waste percentage food: {analysis['highest_waste_percentage_food']}")
        print(f"- Potentially problematic foods: {', '.join(analysis['problematic_foods']) or 'None'}")
        print(f"- Potentially problematic meals: {', '.join(analysis['problematic_meals']) or 'None'}")
    print("\nRecommendations:")
    for recommendation in recommendations:
        print(f"- {recommendation}")
    print(f"\nEstimated Weekly Saving: {_kg(analysis['estimated_weekly_saving'])}")
