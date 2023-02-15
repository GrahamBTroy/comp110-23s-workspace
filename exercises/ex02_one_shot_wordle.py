"""EX02-One Shot Wordle - Loops!"""

___author___ = "730560158"
correct_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
length = 6
print_length = str(length)
word = input("What is your " + print_length + " letter guess? ")
while len(word) != length:
    word = input("That was not " + print_length + " letters! Try again: ")

count = 0
word_index = word[count]
box_storer = ""
playing: bool = True 
Alternative_placement: bool =  False
char_count = 0

while playing:
 while count < len(correct_word): 
    if word[count] == correct_word[count]: 
        box_storer += GREEN_BOX
    else:
        while Alternative_placement == False and char_count < len(correct_word):
            if word[char_count] == correct_word[count]:
                box_storer += YELLOW_BOX
            else:
                box_storer += WHITE_BOX
            char_count = char_count + 1
    count = count + 1
 if len(word) == length: 
   if word == correct_word:  
     print(box_storer)
     print("Woo! You got it! ")
     playing = False
   else:
     print(box_storer)
     print("Not quite. Play again soon!")
 playing = False

