import random

words = ["python", "laptop", "keyboard", "monitor", "printer"]

word = random.choice(words)
guessed = []
wrong = 0

print("Welcome to Hangman!")
print("You get 6 wrong guesses. Good luck.")
print()

while wrong < 6:
    shown = ""
    for ch in word:
        if ch in guessed:
            shown = shown + ch + " "
        else:
            shown = shown + "_ "

    print("Word: " + shown)
    print("Wrong guesses left:", 6 - wrong)

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please type one letter only.")
        print()
        continue

    if guess in guessed:
        print("You already tried that letter.")
        print()
        continue

    guessed.append(guess)

    if guess in word:
        print("Nice, that letter is in the word.")
    else:
        wrong = wrong + 1
        print("Nope, not in the word.")
    print()


    complete = True
    for ch in word:
        if ch not in guessed:
            complete = False

    if complete:
        print("You won! The word was:", word)
        break

if wrong == 6:
    print("Out of guesses. The word was:", word)