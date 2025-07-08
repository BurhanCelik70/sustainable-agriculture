def analyze_soil(pH, moisture, N, P, K):
    messages = []

    # check pH range
    if not (5.5 <= pH <= 7.5):
        messages.append("Check acidity")

    # check moisture level
    if moisture < 30:
        messages.append("Irrigation needed")

    # check nutrient levels
    if N < 50:
        messages.append("Low Nitrogen")
    if P < 30:
        messages.append("Low Phosphorus")
    if K < 20:
        messages.append("Low Potassium")

    # if everything is OK
    if not messages:
        return "Soil conditions are suitable"
    else:
        return ", ".join(messages)

# test with example values
result = analyze_soil(pH=6.5, moisture=28, N=40, P=25, K=18)
print(result)