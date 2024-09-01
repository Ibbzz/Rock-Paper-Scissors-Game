import random
#Import random so a random option can be picked.
#Then we ask if the user wishes to start the game, if the input is "yes" then the game will begin.
#However, if the input is a "no" the game will not begin and infact end.
start = input("Would you like to start the game?\nYes/No\n").lower()
if start == "yes":
    options = ("rock" , "paper" , "scissors")
    running = True

    while running:

        player = None
        computer = random.choice(options)
#Computer picks a random choice, while the users choice is not random.
        while player not in options:
            player = input("Enter a choice (rock, paper , scissors)\n\n").lower()
            print("Pick a Valid option")
#If none out of the Three choices are given by the player, then it will repeat the question till a valid input is given.
        print(f"Player: {player}")
        print(f"computer: {computer}")

        if player == computer:
            print("Its a Tie!\n")
        elif player == "rock" and computer == "scissors":
            print("You Win!\n")
        elif player == "rock" and computer == "paper":
            print("You Lose!\n")
        elif player == "scissors" and computer == "rock":
            print("You Lose!\n")
        elif player == "scissors" and computer == "paper":
            print("You Win!\n")
        elif player == "paper" and computer == "rock":
            print("You Win!\n")
        elif player == "paper" and computer == "scissors":
            print("You Lose!\n")
#Above is the options and anwsers for example if player picks rock and the computer randomly chooses paper, the player will lose.
        continue_game = input("Would you like to play again:\n Y/N\n").lower()
        if not continue_game == "y":
            running = False
#Above the question is asked to the player if they wish to continue with the game, and if they dont the game ends.
    print("Thanks for playing!")


else:
    exit()
