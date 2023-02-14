"""EX02-One Shot Wordle - Loops!"""

___author___ = "730560158"
correct_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word = input("What is your 6 letter guess? ")
count = 0
word_index = word[count]
box_storer = ""
playing: bool = True 

while playing:
 while word_index >= len(correct_word): 
    if word_index == correct_word[count]: 
        append
    count = count+1
 if len(word) != 6:
  word = input("That was not 6 letters! Try again: ")
 if len(word) == 6: 
   if word == correct_word: 
     print("Woo! You got it! ")
     playing = False
   else:
     print("Not quite. Play again soon!")
 playing = False

