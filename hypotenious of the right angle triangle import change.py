import math

a = float(input("Enter the base of the right angle triangle: \n"))
b = float (input("Enter the height of the right angle: \n"))

h = math.sqrt(math.pow(a,2)+math.pow(b,2))

print(f"The hypotenious of the right angle triangle is: \n {h} cm")