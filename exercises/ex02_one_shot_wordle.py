__author__ = "730560158"
"""EX02-One Shot Wordle - Loops!"""
correct_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
length = len(correct_word)
print_length = str(length)
word = input("What is your " + print_length + " letter guess? ")
while len(word) != length:
    word = input("That was not " + print_length + " letters! Try again: ")
## word: str = "pointy"

count: int = 0
word_index = word[count]
box_storer = ""
playing: bool = True 

while playing: 
    while count < len(correct_word): 
        if word[count] == correct_word[count]: 
            box_storer += GREEN_BOX
        else:
            alternative_placement: bool = False
            char_count = 0
            while not alternative_placement and char_count < len(correct_word):
                if word[count] == correct_word[char_count]:
                    alternative_placement = True
                else:
                    char_count = char_count + 1 
            if alternative_placement: 
                box_storer += YELLOW_BOX
            else: 
                box_storer += WHITE_BOX
        count = count + 1
        playing = False
    if len(word) == length: 
        if word == correct_word:  
            print(box_storer)
            print("Woo! You got it! ")
            playing = False
        else:
            print(box_storer)
            print("Not quite. Play again soon!")
            playing = False