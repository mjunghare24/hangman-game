import random

# List of predefined words
words = ['apple', 'banana', 'cherry', 'orange', 'grapes']

# Choose a random word
word = random.choice(words)
guessed_word = ['_'] * len(word)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time. You have 6 incorrect guesses.\n")

while attempts > 0 and '_' in guessed_word:
    print("Word: " + ' '.join(guessed_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Remaining attempts: {attempts}")

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct guess!\n")
    else:
        attempts -= 1
        print("Incorrect guess!\n")

if '_' not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("You ran out of attempts. The word was:", word)