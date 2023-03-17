import random

def number_guessing_game():
    while True:
        random_number = random.randint(1, 100)
        attempts = 0
        
        print("Welcome to the number guessing game! Guess a number between 1 and 100. Type 'quit' or 'exit' to end the game.")
        
        while True:
            user_input = input("Enter your guess: ")
            
            if user_input.lower() in ["quit", "exit"]:
                print(f"Farewell! The correct number was {random_number}.")
                break
                
            try:
                guess = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number or 'quit'/'exit' to end the game.")
                continue
                
            attempts += 1
            
            if guess == random_number:
                print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
                break
            elif guess < random_number:
                print("Too low! Guess higher.")
            else:
                print("Too high! Guess lower.")
                
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye.")
            break

number_guessing_game()