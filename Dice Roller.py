import random

print("🎲 Welcome to Dice Roller!")

while True:
    roll = input("Press Enter to roll the dice (or type 'q' to quit):")

    if roll.lower() =="q":
        print("Quit")
        break

    dice =random.randint(1, 6)
    print("You rolled : ", dice)