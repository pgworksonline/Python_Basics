# Number guessing game to emulate a do-while loop
from random import randint

LOW, HIGH = 1, 10

secret_number = randint(LOW, HIGH)
clue = ""
number_guessed = False

while not number_guessed:
    user_input = input(f"Guess a number between {LOW} and {HIGH} {clue} ")
    number = int(user_input)
    if number > secret_number:
        clue = f"(less than {number})"
    elif number < secret_number:
        clue = f"(greater than {number})"
    else:
        number_guessed = True

print(f"You guessed it! The secret number is {number}")
