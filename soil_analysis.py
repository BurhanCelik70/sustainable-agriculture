def check_irrigation(crop, moisture):
    # minimum moisture levels for each crop type
    thresholds = {
        "wheat": 40,
        "corn": 50,
        "other": 35
    }

    # get threshold based on crop type
    crop = crop.lower()
    if crop in thresholds:
        min_moisture = thresholds[crop]
    else:
        min_moisture = thresholds["other"]

    # compare moisture with threshold
    if moisture < min_moisture:
        return "Irrigation needed"
    else:
        return "No irrigation needed"

# test the function
crop_type = "wheat"
moisture_level = 38
result = check_irrigation(crop_type, moisture_level)
print(result)