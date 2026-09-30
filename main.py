from analyzer import analyze_records
from data_manager import load_records, save_record
from input_handler import prompt_record
from recommendation_engine import generate_recommendations
from report_generator import (print_high_waste, print_intelligence_report,
                              print_recommendations, print_records, print_summary,
                              _print_stats)


def show_menu():
    print("\n" + "=" * 40)
    print("     MESS MEAL WASTE ANALYZER")
    print("=" * 40)
    print("1. Add Meal Record")
    print("2. View Records")
    print("3. Analyze Waste")
    print("4. Food-wise Analysis")
    print("5. Meal-wise Analysis")
    print("6. Day-wise Analysis")
    print("7. High-Waste Records")
    print("8. Recommendations")
    print("9. Complete Intelligence Report")
    print("0. Exit")


def run():
    records = load_records()
    while True:
        show_menu()
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            record = prompt_record()
            save_record(record)
            records.append(record)
            print("Record saved successfully.")
        elif choice == "2":
            print_records(records)
        elif choice == "3":
            print_summary(analyze_records(records))
        elif choice in ("4", "5", "6", "7", "8", "9"):
            analysis = analyze_records(records)
            if choice == "4":
                _print_stats("Food-wise Analysis", analysis["food_stats"])
            elif choice == "5":
                _print_stats("Meal-wise Analysis", analysis["meal_stats"])
            elif choice == "6":
                _print_stats("Day-wise Analysis", analysis["day_stats"])
            elif choice == "7":
                print_high_waste(analysis)
            elif choice == "8":
                print_recommendations(analysis, generate_recommendations(analysis))
            else:
                print_intelligence_report(analysis, generate_recommendations(analysis))
        elif choice == "0":
            print("Thank you for using Mess Meal Waste Analyzer.")
            break
        else:
            print("Invalid choice. Please select a menu number from 0 to 9.")


if __name__ == "__main__":
    run()
