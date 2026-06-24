import random
words = ["python", "computer", "coding", "hangman", "program"]
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)
attempts = 6
guessed_letters = []
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts Left:",attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    if len(guess) !=1 or not guess.isalpha():
        print("Plese eneter a single alphabet. ")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
        for i in range (len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i]= guess
    else:
        attempts -=1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongrats! You successfully guessed the word:", secret_word)
else:
    print("\nGAME OVER!")
    print("The word was:", secret_word)