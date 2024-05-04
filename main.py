from art import logo
import random
from replit import clear

def chose_dificuty(diffi_chose):
    """Chose a difficulty the game"""
    dificult = 0
    if diffi_chose == "easy":
        dificult = 10
    elif diffi_chose == "hard":
        dificult = 5
    return dificult


def chose_number():
    """Chose a number to be guess"""
    number = random.randint(1,100)
    return number
def play_game():
    print(logo)

    print("Welcome To The Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    NUMBER = chose_number()
    print(f"the correct answer {NUMBER}")
    diffi_chose = input("Choose a difficuty. Type 'easy' or 'hard':")
    end_game = False
    dificuty = chose_dificuty(diffi_chose)

    while end_game == False:
        print(f"You have {dificuty} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))
        if NUMBER == guess_number:
            end_game = True
            print(f"You got it. The correct answer is {NUMBER} ")
        elif dificuty == 0:
            end_game = True
            print(f"You lose. The correct answer is {NUMBER}")
        if NUMBER != guess_number:
            if NUMBER > guess_number:
                print("Too Low")
            elif NUMBER < guess_number:
                print("Too high")
            dificuty -= 1
            print("Guess again!")
        clear()
    play_game()

play_game()