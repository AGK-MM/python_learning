# This is the game name
game_name = "Guess the Number"
# This is the number to guess
number_to_guess = 42
# This is the user's guess
user_guess = 0
# This is the main game loop
while user_guess != number_to_guess:
    # Get the user's guess
    user_guess = int(input("Enter your guess: "))
    # Check if the user's guess is correct
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
