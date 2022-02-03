import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for i in range(word_length):
    display.append("_")

wrongGuesses = []

while not game_is_finished:
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in display or guess in wrongGuesses:
    print(f"You've already guessed {guess}")
  for i in range(word_length):
    if guess == chosen_word[i]:
      display[i] = guess
  print(f"{' '.join(display)}")
  if guess not in chosen_word and guess not in wrongGuesses:
    lives -= 1
    wrongGuesses.append(guess)
    print(f"You guessed {guess}, that's not in the word. You have {lives} lives remaining.")
  if lives == 0:
    game_is_finished = True
    print("You lose :(")
    print(f"The word was {chosen_word}")
  if not "_" in display:
    game_is_finished = True
    print("You win!!! :)")
  print(stages[lives])