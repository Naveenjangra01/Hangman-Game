import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'mango', 'strawberry', 'pineapple', 'kiwi', 'papaya', 'pomegranate', 'watermelon']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word

def play_hangman():
    word_to_guess = choose_word()
    max_attempts = 6
    guessed_letters = []
    attempts = 0
    
    print("Welcome to Hangman!")
   
    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("\n Hint:(It's a Fruit name)\n Guess a letter:  ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts += 1
        
        if attempts == max_attempts:
            print("You ran out of attempts. The word was '{}'.".format(word_to_guess))
            break
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word '{}'!".format(word_to_guess))
            break

if __name__ == "__main__":
    play_hangman()
