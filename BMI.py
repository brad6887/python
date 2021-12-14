"""Canadian Computing Competition: 2008 Stage 1, Junior #1
The Body Mass Index (BMI) is one of the calculations used by doctors to
assess an adult's health. The doctor measures the patient's height
(in metres) and weight (in kilograms), then calculates the BMI using the
formula:

BMI = weight / height * height


Write a program which takes the patient's weight and height as input,
calculates the BMI, and displays the corresponding message from the
table below.

BMI Category	                Message
More than25 	                Overweight
Between 18.5 and  (inclusive)	Normal weight
Less than 18.5              	Underweight
"""

weight = input()
height = input()
BMI = int(weight) / (float(height) * (float(height)))

if BMI > 25: 
    print('Overweight')
elif BMI < 18.5:
    print('Underweight')
else:
    print('Normal weight')