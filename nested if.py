response = input("Would you like food? (Y/N): ")

if response == "Y" or response == "y":
    print("Have some food!")
elif response == "N" or response == "n":
    response2 = input("What do you like?\n"
                      "Music (Press M)\n"
                      "Drinks (Press D)\n"
                      "Walking (Press W)\n"
                      "Traveling (Press T)\n"
                      "Painting (Press P): ")
    
    if response2 == "M" or response2 == "m":
        print("Welcome to music")
    elif response2 == "D" or response2 == "d":
        print("Welcome to drinks")
    elif response2 == "W" or response2 == "w":
        print("Welcome to walking")
    elif response2 == "T" or response2 == "t":
        print("Welcome to traveling")
    elif response2 == "P" or response2 == "p":
        print("Welcome to painting")
    else:
        print("Invalid choice")
else:
    print("Naughty")
