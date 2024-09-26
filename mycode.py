# Mad Libs game
# A word game where you create a story by filling the blanks with random words
import os
import time
# Get user inputs
article1 = input("Enter an article (e.g., a, an, the): ")
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a 2nd noun: ")
noun3 = input("Enter a 3rd noun: ")
adjective2 = input("Enter another adjective (description): ")
verb1 = input("Enter a verb ending in -ing: ")
adjective3 = input("Enter one more adjective (description): ")
#Clearing the screen
time.sleep(1)  # Wait for 1 second before clearing the screen
os.system('cls' if os.name == 'nt' else 'clear')  # Clear command for Windows ('cls') and for Unix/Linux/MacOS ('clear')

# Construct and print the story
print(f"Today I went to {article1} {adjective1} {noun1}.")
print(f"In an exhibition, I saw {noun2}.")
print(f"{noun3} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!")