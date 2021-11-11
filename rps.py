import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = ", ".join(random.choices(choices))
    player = input("rock, paper, scissors? ").lower()
    
    while player not in choices:
        player = input("rock, paper, or scissors? ").lower()

    if player == computer:
        print("shoot!")
        print("computer:", computer)
        print("player:", player)
        print("tie! :0")

    elif player == "rock":
        if computer == "paper":
            print("shoot!")
            print("computer:", computer)
            print("player:", player)
            print("you lose! D:")
        if computer == "scissors":
            print("shoot!")
            print("computer:", computer)
            print("player:", player)
            print("you win! :D")

    elif player == "paper":
        if computer == "scissors":
            print("shoot!")
            print("computer:", computer)
            print("player:", player)
            print("you lose! D:")
        if computer == "rock":
            print("shoot!")
            print("computer:", computer)
            print("player:", player)
            print("you win! :D")

    elif player == "scissors":
        if computer == "rock":
            print("shoot!")
            print("computer:", computer)
            print("player:", player)
            print("you lose! D:")
        if computer == "paper":
            print("shoot!")
            print("computer:", computer)
            print("player:", player)
            print("you win! :D")

    repeat = input("would you like to play again? (yes/no): ").lower()
    if repeat != "yes":
        break

print("yer done :p")
