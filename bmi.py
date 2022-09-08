height = input("Enter Your Height: ")
weight = input("Enter Your Weight: ")
bmi=int(weight)/float(height)**2
bmi_as_int=int(bmi)
print("you have",bmi_as_int,"BMI")