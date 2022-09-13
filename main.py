# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


result1 = int(weight)
result2 = float(height)

result3 = result1 / result2 ** 2

result = int(result3)

print(result)

if result < 18.5:
  print(f'Your BMI is {result}, you are underweight')
elif result < 25:
  print(f'Your BMI is {result}, you have a normal weight')
elif result < 30:
    print(f'Your BMI is {result}, you are slightly overweight')
elif result < 35:
    print(f'Your BMI is {result}, you are obese')
elif result > 35:
  print(f'Your BMI is {result}, you are clinically obese')
 


  

