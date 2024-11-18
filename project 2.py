#guess the number 
import random

def Guess_the_number():
    number_to_guess = random.randint(1, 100) 
    attempts=10
    print("welcome to the Guess the number!".title())
    print("i have chosen a number between 1 to 100".title())
    print(f"you have{attempts} attempts to guess the number".title())
    for attempts in range(1,attempts+1):
        guess = int(input(f"Attempt{attempts}:enter your guess:".upper()))
        if guess<number_to_guess :
            print("your guess is to low.")
        elif guess>number_to_guess:
            print("your guess is to high.")
        else:
             print(f"congratulations! you have guessed the number in {attempts} attempts".upper())
             break
    else:
        print(f"you used all your attempts.the number was = {number_to_guess}.".upper())
Guess_the_number()
            
    