#!/usr/bin/env python3
import random

class Hangman:
    def __init__(self, trials):
        self.trials = trials
        self.word = None
        self.revealed_letters = []

    def set_word(self):
        words = ['meat', 'meet', 'repeat', 'speed', 'heet']
        self.word = random.choice(words)  # Select one word randomly
        self.revealed_letters = list(self.word[:2])  # Reveal the first two letters

    def get_word(self):
        return self.revealed_letters

    def guess_rest(self, guess):
        if guess in self.word[2:]:
            return True
        else:
            self.trials -= 1
            return False

trials = 3

game = Hangman(trials)
game.set_word()
print("Revealed letters:", game.get_word())

# Example loop to simulate multiple guesses
while game.trials > 0:
    guess = input("Guess a letter or remaining part: ")
    if game.guess_rest(guess):
        print("Correct guess!")
        break
    else:
        print("Wrong guess. Remaining trials:", game.trials)

if game.trials == 0:
    print("Game Over! The word was:", game.word)

