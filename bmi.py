def calculate_bmi(height, weight): 
    print("height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height*height)
    print("BMI IS" ,BMI)
    if (BMI<18.5):
        print("you are underweight")
    elif (BMI>=18.5 and BMI<=25.0):
        print("you are normal weight")
    else:
        print("you are overwight")


calculate_bmi(weight = 57, height=1.73)

