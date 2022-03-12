#GUESS THE NUMBER GAME

from art import logo
from replit import clear
import random

def guess_the_number_game(): #function created for recursion
    clear()
    print(logo)

    #Define variables
    correct_number = random.choice(range(1,101))
    NUM_ATTEMPTS_EASY = 10
    NUM_ATTEMPTS_HARD = 5

    #Define functions used
    def how_many_attempts():
        """Outputs number of total attempts for easy or hard difficulty level"""
        if difficulty == "easy":
            return NUM_ATTEMPTS_EASY
        elif difficulty == "hard":
            return NUM_ATTEMPTS_HARD
        else:
            print("\nInvalid input. Let's set your difficulty to 'hard'.")
            return NUM_ATTEMPTS_HARD
    
    def too_low():
        """Returns a message to the user when the guess is too low"""
        return "Too low."
        
    def too_high():
        """Returns a message to the user when the guess is too high"""
        return "Too high."

    #Begin the game...
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.\n")
    #print(f"Pssst, the correct number is {correct_number}.") #testing code
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    remaining_attempts = how_many_attempts()
    
    end_of_game = False
    while end_of_game == False:
        print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        guess = int(input("\nMake a guess: "))
        #The user guesses an incorrect number      
        if guess != correct_number:
            remaining_attempts -= 1
            if guess > correct_number:
                print(too_high())
            elif guess < correct_number:
                print(too_low())
            if remaining_attempts == 0: #run out of attempts
                print(f"\nYou've run out of guesses. You lose. 😢 The answer was {correct_number}.")
                end_of_game = True
        #The user guesses the correct number
        else:
            print(f"You got it! 😁 The answer was {correct_number}.")
            end_of_game = True

    #Play again?
    play_again = input("\nWould you like to play again? Type 'y' or 'n': ").lower()
    if play_again == "y":
        guess_the_number_game()

guess_the_number_game()