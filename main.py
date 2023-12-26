# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi=weight/height**2
whole_bmi=int(bmi)

if whole_bmi<18.5:
    print(f"Your BMI is {whole_bmi}, you are underweight.")
elif 18.5<whole_bmi<25:
    print(f"Your BMI is {whole_bmi}, you have normal weight.")
elif 25<whole_bmi<30:
    print(f"Your BMI is {whole_bmi}, you are slightly overweight.")
elif 30<whole_bmi<35:
    print(f"Your BMI is {whole_bmi}, you are obese.")
else:
    print(f"Your BMI is {whole_bmi}, you are slightly overweight.")



