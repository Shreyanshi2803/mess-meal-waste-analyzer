# Mess Meal Waste Analyzer

## Project Overview

Mess Meal Waste Analyzer is a beginner-friendly Python command-line project for studying food waste in a college mess. It stores meal records in CSV format, calculates waste values, finds patterns, classifies waste severity, and creates rule-based recommendations.

## Features

- Add and view meal records
- Calculate prepared, consumed, and wasted quantities
- Calculate waste percentages and LOW/MODERATE/HIGH/CRITICAL status
- Analyze food, meal, and date totals
- Find highest and lowest waste items
- Detect high-waste and unusual records
- Generate recommendations and an intelligence report
- Estimate possible weekly savings
- Handle invalid input, missing files, empty files, and corrupted rows

## Technologies / Tools Used

- Python standard library
- CSV files
- `unittest`
- VS Code
- Git/GitHub

No external packages are required. `requirements.txt` is intentionally minimal.

## Project Structure

- `main.py`: menu and application flow
- `models.py`: `MealRecord` data structure
- `input_handler.py`: user prompts
- `validator.py`: input validation rules
- `data_manager.py`: CSV loading and saving
- `waste_calculator.py`: independent waste calculations and thresholds
- `analyzer.py`: food, meal, date, pattern, and summary analysis
- `recommendation_engine.py`: transparent rule-based recommendations
- `report_generator.py`: readable terminal reports
- `data/meal_data.csv`: live application data
- `data/sample_data.csv`: demonstration records
- `tests/`: built-in unit tests

The analysis uses simple loops and dictionaries. Each dataset is scanned a small number of times, so the main aggregation is approximately O(n) for n records.

## Installation

1. Install Python 3.
2. Open or download this project folder in VS Code.
3. Open a terminal in `mess_meal_waste_analyzer`.
4. No package installation is needed.

To use the supplied demonstration data, copy `data/sample_data.csv` over `data/meal_data.csv` before running the program. Keep the original sample file unchanged.

## How to Run

From the project root:

```text
python main.py
```

## How to Test

From the project root:

```text
python -m unittest discover
```

## Sample Usage

After loading the supplied sample data, choose option `9`.

```text
Total Prepared: 351.00 kg
Total Consumed: 273.00 kg
Total Wasted: 78.00 kg
Overall Waste Rate: 22.2%
Waste Status: MODERATE
Highest Waste Food: Rice
Highest Waste Meal: Dinner
```

The exact report also includes problematic foods or meal periods, unusual records, recommendations, and an estimated weekly saving calculated from the records.

## Error Handling

The program validates dates, meal types, food names, numeric quantities, negative values, and the rule that consumed food cannot exceed prepared food. Invalid menu choices do not stop the program. Missing, empty, or malformed CSV rows are skipped safely.

## Future Enhancements

- Export reports to a text or CSV file
- Add charts using an optional visualization package
- Track meal attendance and cost savings
- Add a configurable settings file for thresholds
