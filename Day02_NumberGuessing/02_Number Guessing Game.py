import random

def play_game():
    difficulty = input("Choose your difficulty level: easy / medium / hard / custom 😊 : ")
    if difficulty == "easy":
        start, end = 1, 50
    elif difficulty == "medium":
        start, end = 1, 100
    elif difficulty == "hard":
        start, end = 1, 500
    else:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

    comp = random.randint(start, end)
    guesses = 0
    player_guess = None

    print(f"Guess the number between {start} and {end}:")

    while player_guess != comp:
        try:
            player_guess = int(input("Your guess: "))
            guesses += 1

            if comp > player_guess:
                print("⬆️  Higher number please!\n")
            elif comp < player_guess:
                print("⬇️  Lower number please!\n") 
            else:
                print(f"🎯 You guessed the number in {guesses} guesses! 👌")
        except ValueError:
            print("❌ Please enter a valid integer!")

while True:
    play_game()
    choice = input("Do you want to play again? (y/n): ").lower()
    if choice != 'y':
        print("See you soon, gentleman 👋🏻")
        break
