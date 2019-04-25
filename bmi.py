weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in m): "))
bmi = (weight) / ((height)**2)
print ("Your BMI is: ", bmi)
if bmi < 18.5:
    print ("You are underweight!!")
elif bmi > 24.9:
    print ("You are overweight!!")
else:
    print ("You are normal!!")

