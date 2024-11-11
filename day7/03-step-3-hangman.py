word_list = [ "python", "java", "typescript" ]

import random

chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
  guess = input("Guess a letter: ").lower()

  display = ""

  for letter in chosen_word:
      if letter == guess:
          display += letter
          correct_letters.append(letter)
      elif letter in correct_letters:
          display += letter
      else:
          display += "_"

  print(display)

  if "_" not in display:
      game_over = True
      print("You win!")