weight=float(input("please enter your weight(kg)"))
height=float(input("please enter your height(m)"))
#let users imput their self information
BMI=weight/(height**2)
#use the formula to caculate BMI
BMI=round(BMI,2)
#get a round number
if BMI>30:
    print("your BMI is",BMI,", you are obese")
elif BMI<18.5:
    print("your BMI is",BMI,", you are underweight")
else:
    print("your BMI is",BMI,", you are normal weight")
#using BMI to judge the body weight and export