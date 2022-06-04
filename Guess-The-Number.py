import random

top_of_range = input("enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0(zero).")
        quit()

else:
    print("Please enter a number.")
    quit()

random_number = random.randint(0, top_of_range)

num_of_guesses = 0
chances = 8

while chances > 0:
    num_of_guesses += 1
    chances = chances - 1
    user_guess = input("Guess the number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number.")
        continue

    if user_guess == random_number:
        print("You got the guess correct!")
        break

    elif user_guess > random_number:
        print("Your guess is above the correct number!")
        print("Only " + str(chances) + " Chances left ")

    else:
        print("Your guess is below the correct number!")
        print("Only " + str(chances) + " Chances left ")

print("You guessed the number correct in", num_of_guesses, "guesses.")
