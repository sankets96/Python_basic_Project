import random
options= ("rock","paper","scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter the choise (Rock , Paper, Scissors):")
        print(f"player:{player}")

        if player == computer:
            print("Its a Tie !")
        elif player == 'rock' and computer=='scissors':
            print("You Win !")

        elif player=='paper' and computer=='rock':
            print("You Win !")
        elif player=='scissors' and computer=='paper':
            print("You Win !")
        else:
            print("You Lose !")

        if not input("Play Again [Y/N] :").lower() == 'y':
            running=False
    
    print("Thank you Playing")