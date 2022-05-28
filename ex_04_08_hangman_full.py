#!/usr/bin/python
import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 14
guessed_letters = ''

def play():
  word = pick_a_word()
  while True:
    guess = get_guess(word)
    if process_guess(guess, word):
      print('You win! Well Done!')
      break
    if lives_remaining == 0:
      print('You are Hung!')
      print('The word was: ' + word)
      break
      
def pick_a_word():
  return random.choice(words)

def get_guess(word):
  print_word_with_blanks(word)
  print('Lives Remaining: ' + str(lives_remaining))
  guess = input('Guess a letter or whole word?')
  return guess

def print_word_with_blanks(word):
  display_word = ''
  for letter in word:
    if guessed_letters.find(letter) > -1:
      # letter found
      display_word = display_word + letter
    else:
      # letter not found
      display_word = display_word + '-'
  print (display_word)

def process_guess(guess, word):
  if len(guess) > 1:
    return whole_word_guess(gyess, word)
  else:
    return single_letter_guess(guess, word)
