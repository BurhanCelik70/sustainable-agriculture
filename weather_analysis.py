def should_spray(temp, humidity, wind_speed, rain_prob):
    if temp > 38:
        return "No Spray: Too hot"
    if wind_speed > 20:
        return "No Spray: Wind too strong"
    if rain_prob > 30:
        return "No Spray: Rain likely"
    if humidity < 30:
        return "No Spray: Low humidity"
    return "Spray: Weather is okay"

# test values to check if spraying is safe
temp = 32
humidity = 50
wind_speed = 10
rain_prob = 15

result = should_spray(temp, humidity, wind_speed, rain_prob)
print(result)