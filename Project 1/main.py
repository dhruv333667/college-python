import random

# Game choices
choices = {
    's': 1,  # Snake
    'w': -1, # Water
    'g': 0   # Gun
}

reverse_choices = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# Random choice for the computer
computer = random.choice(list(choices.values()))

# User input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Input validation
if youstr not in choices:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = choices[youstr]

    # Display choices
    print(f"You chose {reverse_choices[you]}\nComputer chose {reverse_choices[computer]}")

    # Determine the outcome
    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You win!")
    else:
        print("You lose!")
