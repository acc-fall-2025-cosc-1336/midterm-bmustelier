from question_a import get_random_number

def main():
    number = get_random_number()
    while True:
        guess = input("Guess a number between 1 and 5 (or 'q' to quit): ").strip()
        if guess.lower() == 'q':
            print("Goodbye!")
            break
        try:
            guess_int = int(guess)
        except ValueError:
            print("Please enter a valid integer between 1 and 5, or 'q' to quit.")
            continue
        if not 1 <= guess_int <= 5:
            print("Please enter a number between 1 and 5.")
            continue
        if guess_int == number:
            print("Congratulations! You guessed it.")
            number = get_random_number()
        else:
            print("Sorry, try again.")

if __name__ == "__main__":
    main()