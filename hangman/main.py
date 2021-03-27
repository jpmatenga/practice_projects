import random
from words import words

def hangman():
    """Function for hangman game"""

    secret = random.choice(words)  # select a random word from the words list
    while '-' in secret or ' ' in secret:  # ensures that the words from the list dont have spaces or -'s
        secret = random.choice(words)

    wrong_guess = 8
    guesses = []
    done = False

    while not done:
        for letter in secret:  # will print a correct guess and a - for a missing letter
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("-", end=" ")
        print("")

        guess = input(f"You have {wrong_guess} guesses left. Pick a letter: ")
        guesses.append(guess.lower())  # places correct letter into guess list
        if guess.lower() not in secret.lower():
            wrong_guess -= 1  # if guess is wrong lose a life
            if wrong_guess == 0:
                break

        done = True
        for letter in secret:
            if letter.lower() not in guesses:
                done = False

    if done:
        print(f"You guessed the word. It was {secret}")
        play_again = input("Would you like to play again? Enter 'y' for yes or 'n' for no")
        if play_again == "y":
            hangman()
        else:
            print("Thanks for playing")

    else:
        print(f"You lose. The word was {secret}")
        play_again = input("Would you like to play again? Enter 'y' for yes or 'n' for no: ")
        if play_again == "y":
            hangman()
        else:
            print("Thanks for playing")


hangman()