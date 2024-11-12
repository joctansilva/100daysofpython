import random
import hangman_worlds
import hangman_stages
import hangman_logo

lives = 7

print(hangman_logo.logo)

chosen_word = random.choice(hangman_worlds.word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(f"Your word to guess is {placeholder}")

game_over = False
correct_letters = []

while not game_over:
  print(f"\n************************* {lives} / 7 lives remains *************************")
  guess = input("\nPlease Guess a letter: ").lower()
  if guess in correct_letters:
      print(f'You already guessed that letter "{guess}"!')
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
  
  if guess not in chosen_word:
      lives -= 1
      print(f"You guessed {guess}, that's not in the word. You love a life")
      if lives == 0:
          game_over = True
          print(f"************************* IT WAS NOT A {chosen_word}, YOU LOSE! *************************")

  if "_" not in display:
      game_over = True
      print("*************************a YOU WIN! *************************{")

  print(hangman_stages.stages[lives]) 