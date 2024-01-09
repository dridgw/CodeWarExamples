while True:
    import random as ran, Hangman.hangman_stages as hs, sys
    #List of random words
    words = ["tiger","tree","underground","giraffe","chair"]

    #Function to select a random word from the word list
    def select_word(words):
        return ran.choice(words)

    remaining_attempts = 6
    guessed_letters = ""

    def print_secret_word(secret_word, guessed_letters):
        for letter in secret_word:
            if letter in guessed_letters:
                print(" {} ".format(letter), end="")
            else:
                print(" _ ", end="")
        print("\n")

    def is_guess_in_secret_word(guess, secret_word):
        if len(guess)> 1 or not guess.isalpha(): # This code ensures that the input is a single character. The isalpha() method ensures the character is alphabetic
            print("Only single letters are allowed. Unable to continue")
            sys.exit()
        else:
            if guess in secret_word:
                return True
            else:
                return False

    def get_unique_letters(word):
        return "".join(set(word)) # returns a string with the unique characters of word in an arbitrary order


    print("Welcome to the Hangman Game! Let's see if you can guess this word!\n")
    secret_word = select_word(words)

    while remaining_attempts > 0 and len(guessed_letters) < len(get_unique_letters(secret_word)):
        guess = input("Guess a letter: ")
        guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

        if guess_in_secret_word:
            if guess in guessed_letters:
                print("You have already guessed the letter {}".format(guess))
            else:
                print("Yes! The letter {} is part of the secret word".format(guess))
                guessed_letters += guess
        else:
            print("No! The letter {} is not part of the secret word".format(guess))
            remaining_attempts -= 1

        print(hs.get_hangman_stage(remaining_attempts))
        print("\n{} attempts remaining\n".format(remaining_attempts))
        print_secret_word(secret_word, guessed_letters)
        print("\n\n Number of letters guessed: {}\n".format(len(guessed_letters)))

    if len(guessed_letters) == len(get_unique_letters(secret_word)):
        print("+++ Well done, you have won this game! +++\n")
    else:
        print("--- Sorry, you have lost this game! ---\n")

    play_again = input("Would you like to play again? Yes(y) or no(n)")
    
    if play_again.lower() == "n":
        break
    elif play_again.lower() =="y":
        continue
