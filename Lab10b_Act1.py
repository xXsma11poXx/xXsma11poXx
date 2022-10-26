
import random
# imports and sets random number variable
num = random.randint(1, 100)
num2 = random.randint(1, 7)

# gives a hint after five failed attempts
def hint():
    a = num + num2
    b = num - num2
    print(f"Here's a hint\nThe number is between {b} and {a}")

# prints out menu to guide players
def welcome_menu():
    print("Welcome to Nick's guessing game!\nOur featured game today is the number guessing game!\n"
          "There are only two rules!\n*****You have to guess a number in between 1 and 100*****\n*****Have fun!*****")

# message for winner
def winner():
    print(f"CONGRATULATIONS!\n****YOU WON****\nThe secret number was {num}!")
    print(f'You guessed {count} times!')


welcome_menu()

val = False
count = 1
x = int(input('Pick a number:'))
# loop that asks for numbers until value is guessed
while val is False:
    count += 1
    if x < 0 or x > 100:
        print("Remember the number is inbetween 1 and 100!")
    print('You guessed it!') if x == num else print(
        "You're too high!") if x > num else print("You're too low!")
    x = int(input('Guess again!:'))
    if count == 5 and x != num:
        hint()
    if x == num:
        val = True
        winner()
