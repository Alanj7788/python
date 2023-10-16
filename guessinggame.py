import random

secret_number = [7, 8, 9]
comp_choice = random.choice(secret_number)
i = 1

while i <= 3:
    user_input = int(input(f"Choice {i}: "))
    if user_input == comp_choice:
        print("You win")
        break  # Exit the loop if the user guessed correctly
    else:
        print(f"You Lose...Computer choice was {comp_choice}")
        i = i + 1

if i > 3:
    print("You've run out of chances. The correct answer was", comp_choice)
