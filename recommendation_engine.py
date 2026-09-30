def generate_recommendations(analysis):
    if not analysis["record_count"]:
        return ["Add meal records to generate recommendations."]
    recommendations = []
    status = analysis["overall_status"]
    if status == "LOW":
        recommendations.append("Overall waste is low. Continue the current preparation and monitoring routine.")
    elif status == "CRITICAL":
        recommendations.append("Critical warning: review portion planning and leftover handling immediately.")
    else:
        recommendations.append("Track the highest-waste items closely and adjust preparation in small steps.")
    if analysis["problematic_foods"]:
        foods = ", ".join(analysis["problematic_foods"])
        recommendations.append(f"Reduce preparation quantities gradually for consistently high-waste foods: {foods}.")
    if analysis["problematic_meals"]:
        meals = ", ".join(analysis["problematic_meals"])
        recommendations.append(f"Review serving forecasts for these meal periods: {meals}.")
    if analysis["highest_waste_day"] != "None":
        day = analysis["highest_waste_day"]
        recommendations.append(f"Investigate {day}, which has the highest recorded total waste.")
    if analysis["unusual_records"]:
        recommendations.append("Check unusual records for attendance changes, menu preferences, or preparation issues.")
    return recommendations
