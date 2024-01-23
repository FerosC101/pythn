import math

print('**********BMI CALCULATOR**********\n')

print('Hello Welcom to the BMI Calculator\n')
name = str(input('What is your name?: '))

print('Hello', name, '\n')

Weight = int(input('Enter your weight in kilograms: '))
Height = float(input('Enter your height in meters: '))
print(" ")

BMI = Weight/(math.pow(Height, 2))

if (BMI < 18.5):
    result = 'you are underweight!'
elif (BMI >= 18.5 and BMI < 25.0):
    result = 'you are Healthy!'
elif (BMI >= 25.0 and BMI < 30.0):
    result = 'you are overwieght!'
elif (BMI >= 30):
    result = 'you are obese!'
else:
    print('Invalid Input')


print('Hello', name, 'Your BMI is', round(BMI, 2), result)

