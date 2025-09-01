# Rock Paper Scissors Game
from random import randint

# Player

moves = ["rock", "paper", "scissor"]

while True:
    computer = moves[randint(0,2)]
    player = input("Rock Paper Scissors or End The Game  ").lower()
    if player == "end the game":
        print("Game Over")
        break
    elif player == "rock":
        if computer == "paper":
            print("You Lose", computer, "beats", player)
        elif computer == "scissor":
            print("You Win", player, "beats", computer)
        else:
            print("Its A Tie")
    elif player == "paper":
        if computer == "scissor":
            print("You Lose", computer, "beats", player)
        elif computer == "rock":
            print("You Win", player, "beats", computer)
        else:
            print("Its A Tie")
    elif player == "scissor":
        if computer == "scissor":
            print("Its A Tie")
        elif computer == "rock":
            print("You Lose", computer, "beats", player)
        else:
            print("You Win", player, "beats", computer)
    else:
        print("Do you mean scissor instead of siscors")