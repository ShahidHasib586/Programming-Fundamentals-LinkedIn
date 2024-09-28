age = int(input("Enter your age: "))

if  age >= 18 and age <100:
    print ("You are now signed up!")   
elif age <=0:
    print ("You havent been born yet")
elif age >=100:
    print("you are too old to sign up")
else:
    print ("Fuck off!")