import random

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("You have to guess a number between 1 and 100.")
    print("You have 10 attempts. Let's get started!\n")

def get_user_name():
    return input("Please enter your name: ")

def generate_random_number():
    return random.randint(1, 100)

def play_game():
    random_number = generate_random_number()
    attempts = 10

    while attempts > 0:
        user_guess = int(input(f"Attempts left: {attempts}. Enter your guess: "))

        if user_guess == random_number:
            print("Congratulations! You guessed the number correctly. You win!")
            return True
        elif user_guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        attempts -= 1

    print(f"\nGame over. The number was {random_number}. Better luck next time!")
    return False

def main():
    display_welcome_message()
    user_name = get_user_name()
    play_again = True

    while play_again:
        play_again = play_game()
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False

    print(f"\nThank you for playing, {user_name}. Goodbye!")

if __name__ == "__main__":
    main()
