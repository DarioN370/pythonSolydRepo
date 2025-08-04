# MATH OPERATORS / Base to imc calc
# num1 = int(input('Type your number: '))
# num2 = int(input('Type your number: '))
# add = num1 + num2
#
# print('your sum is: ' + str(add))
#----------------------------------- IMC Calculator --------------------------------------

weight = float(input('Type your weight in kg: '))
height = float(input('Type your height in m: '))
bmi = weight / (height * height)


print('\n ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘'
    '\n Your BMI is: ' + str(bmi) +
      '\n ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘'
      '\n <18.5 = Underweight '
      '\n 18.5 - 24.9 = Normal'
      '\n 25 - 29.9 = Overweight'
      '\n >= 30 = Obesive'
      )
