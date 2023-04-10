"""EX03 - Structured Wordle"""
__author__ = "730561058"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#setting up variables
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
            if contains_char(correct_word, inputed_word[count]) == True: 
                box_storer += YELLOW_BOX
            else:
                box_storer += WHITE_BOX
        count = count + 1
    return box_storer

def input_guess(input_guess: int) -> str:
    game = True
    while game == True:
        guess: str = input("Enter a " + str(input_guess) + " character word: ") 
        if len(guess) == input_guess: 
            game = False
        else: 
            print("That wasn't " + str(input_guess) + " chars! Try again: ")
    return guess 
 
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    count = 1
    game: bool = True
    true_word: str = "codes"  
    char_count: int = 5
    N = 6
    while count <= N and game == True: 
        print("=== Turn " + str(count) + "/" + str(N) + " ===" )
        guess = input_guess(char_count)
        print(emojified(guess, true_word))
        if guess == true_word:
            print("You won in " + str(count) + "/" + str(N) + " turns!")
            game = False
        count = count + 1
    if count > N:
        print("X/" + str(N) + " - Sorry, try again tomorrow!")
    game = False

if __name__ == "__main__":
    main()
    


