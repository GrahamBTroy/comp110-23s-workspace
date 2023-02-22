"""EX03 - Structured Wordle"""
__author__ = "730561058"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(inputed_word: str, inputed_letter: str) -> bool:
    count: int = 0
    assert len(inputed_letter) == 1
    while count < len(inputed_word):
        if inputed_letter == inputed_word[count]: 
            return True
        count = count + 1 
    return False
        
def emojified(inputed_word: str, correct_word: str) -> str: 
    count: int = 0
    box_storer: str = ""
    assert len(inputed_word) == len(correct_word)
    while count < len(inputed_word): 
        if inputed_word[count] == correct_word[count]: 
            box_storer += GREEN_BOX  
        else: 
            contains_char
            if contains_char == True: 
                box_storer += YELLOW_BOX
            elif contains_char == False:
                box_storer += WHITE_BOX
        count = count + 1
    return box_storer
 
    

# setting up variables
