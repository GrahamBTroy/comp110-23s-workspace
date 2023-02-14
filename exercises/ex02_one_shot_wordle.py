"""EX02-One Shot Wordle - Loops!"""

___author___ = "730560158"
correct_word = "dragon"
word = input("What is your 6 letter guess? ")
playing: bool = True 

while playing:
 if len(word) != 6:
  word = input("That was not 6 letters! Try again: ")
 if len(word) == 6: 
   if word == correct_word: 
     print("Woo! You got it! ")
     playing = False
   else:
     print("Not quite. Play again soon!")
 playing = False

