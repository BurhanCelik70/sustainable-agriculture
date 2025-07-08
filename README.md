# Sustainable Agriculture – Smart Farming Support Project

This is a beginner-level personal project where I developed simple Python functions to support smart farming decisions.  
The goal is to help farmers make quick, logic-based decisions using basic weather and soil data.

---

## 🌱 Features

### 1. Weather Analysis and Visualization
- Normalizes weather data such as temperature, humidity, wind speed, and rain probability
- Uses `matplotlib` to graph and visualize normalized features
- Helps understand patterns and compare variables

### 2. Spraying Decision Function
- Determines whether it's safe to spray pesticide
- Checks conditions like temperature, wind speed, humidity, and chance of rain
- Returns messages like `"Spray: Weather is okay"` or `"No Spray: Wind too strong"`

### 3. Soil Condition Checker
- Analyzes soil pH, moisture, and nutrient levels (N, P, K)
- Gives recommendations like `"Check acidity"`, `"Irrigation needed"`, or `"Low Nitrogen"`

### 4. Irrigation Recommendation
- Suggests irrigation based on crop type and soil moisture level
- Supports crops like wheat, corn, and others
- Helps reduce water waste and increase efficiency

---

## 🧰 Technologies Used
- Python
- Matplotlib
- Scikit-learn (for MinMaxScaler)
- NumPy

---

## 💻 How to Run

Clone or download this repository and run the `.py` files in a Python IDE (like Thonny, VSCode, or IDLE).

```bash
python weather_analysis.py
python spray_decision.py
python soil_analysis.py
python irrigation_check.py
