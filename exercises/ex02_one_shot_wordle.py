"""EX02-One Shot Wordle - Loops!"""

___author___ = "730560158"
correct_word = "python"
word = "What is your 6 letter guess?"

if len(word) != 6:
 print("That was not 6 letters! Try again:")
while len(word) == 6: 
  if word == correct_word: 
    print("Woo! You got it!")
  else:
    print("Not quite. Play again soon!")

