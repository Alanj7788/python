import random

def get_choices():
    player_choice=input("Enter a choice(rock,scissor,paper): ")
    options=["rock","paper","scissor"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"You chose {player},Computer chose {computer}")
    if player==computer:
        return "its a tie"
    elif player=="rock":
        if computer=="scissor":
            return "You win"
        else:
            return "You lose"
    elif player=="paper":
        if computer=="scissor":
            return "You lose"
        else:
            return "You win"
    else:
        if computer=="paper":
            return "You win"
        else:
            return "You lose"
        
choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)
    
