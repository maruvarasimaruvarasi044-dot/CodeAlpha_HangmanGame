import random

def hangman_game():
    # 5 predefined words list
    words = ["python", "coding", "intern", "alpha", "script"]
    
    # Random-ah oru word choose pannuthu
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6
    
    print("--- WELCOME TO HANGMAN GAME ---")
    print("Guess the word, one letter at a time.")
    
    while attempts_left > 0:
        # Player-ku blank spaces display panrathu
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord: ", display_word.strip())
        print(f"Attempts left: {attempts_left}")
        
        # Word full-ah guess pannitangala nu check panna
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break
            
        # User kitta irunthu letter vaanguthu
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
            
        guessed_letters.append(guess)
        
        # Letter word-la irukaa nu check panrathu
        if guess in secret_word:
            print("Good guess! That letter is in the word.")
        else:
            print("Wrong guess!")
            attempts_left -= 1
            
    if attempts_left == 0:
        print(f"\n😢 Game Over! The correct word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    hangman_game()
