weight = float(input("Enter your weight: "))
unit = input("(L)bs or(K)g: ")
if unit.upper() == "L" :
 converted = weight * 0.45
 print(f"you are {converted} kilograms")
else:
    converted = weight /0.45
    print(f"you are {converted} pounds ")