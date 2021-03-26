import random # cpu picks random number

player_score = 0 # keeps score between computer and player
cpu_score = 0

while True:
    #loop continues until a winner is declared
    player_choice = int(input("Choose 1 for rock, 2 for paper and 3 for scissors: "))
    cpu_choice = random.randint(1, 3) # cpu randomly selects a number between 1 and 3

    # game logic
    if player_choice == cpu_choice:
        print("Its a tie. try again")

    elif player_choice == 1:
        if cpu_choice == 2:
            print("Cpu chose paper, you lose")
            cpu_score += 1
            print(f"Cpu {cpu_score} - player score {player_score}")

        if cpu_choice == 3:
            print("Cpu chose scissors, you win")
            player_score += 1
            print(f"Cpu {cpu_score} - player score {player_score}")

    elif player_choice == 2:
        if cpu_choice == 1:
            print("Cpu chose rock, you win")
            player_score += 1
            print(f"Cpu {cpu_score} - player score {player_score}")

        if cpu_choice == 3:
            print("Cpu chose scissors, you lose")
            cpu_score += 1
            print(f"Cpu {cpu_score} - player score {player_score}")

    elif player_choice == 3:
        if cpu_choice == 1:
            print("Cpu chose rock, you lose")
            cpu_score += 1
            print(f"Cpu {cpu_score} - player score {player_score}")

        if cpu_choice == 2:
            print("Cpu chose paper, you win")
            player_score += 1
            print(f"Cpu {cpu_score} - player score {player_score}")

    # declaring a winner and breaking the loop

    if player_score == 2:
        print(f"You scored {player_score} out of 3, you win")
        break
    if cpu_score == 2:
        print(f"The CPU scored {cpu_score} out of 3, you lose")
        break
