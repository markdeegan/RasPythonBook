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
  print('word with blanks')
  print('Lives Remaining: ' + str(lives_remaining))
  guess = input('Guess a letter or whole word?')
  return guess
