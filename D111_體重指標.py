def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 3)

def determine_weight_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 23.0:
        return "Normal"
    elif bmi < 25.0:
        return "Overweight"
    else:
        return "Obese"


weight, height = map(float, input().split())

bmi = calculate_bmi(weight, height)

weight_status = determine_weight_status(bmi)

print("{:.3f}".format(bmi))
print(weight_status)