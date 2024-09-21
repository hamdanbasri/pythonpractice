weight = int(input("What is your weight? "))
type = input("(K)g or (L)bs? ")
if type.upper() == "K":
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kg is:" + str(converted))