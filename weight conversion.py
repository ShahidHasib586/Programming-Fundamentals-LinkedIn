#lb to kg or kg to lb converter
select = input("Choose one option: \n For lb to kg pess 1:  \n For kg to lb pess 2: ")
weight = float(input ("Enter the weight: "))

if select == "1":
    weight = weight/2.205
    print(f"Your weight is {weight} kg")
elif select == "2":
    weight = weight*2.205
    print(f"Your weight is {weight} lb")
    
else:
    print("Invalid Input")