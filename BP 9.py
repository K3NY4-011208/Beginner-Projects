import random

while True:
    roll = input("Press Enter to roll the dice or type 'q' to quit: ").lower()
    if roll == "q":
        print("Goodbye!")
        break
    print("You rolled:", random.randint(1, 6))
