"""EX06 - choose your own adventure."""
__author__ = "730561058"
points: int = 0
player: str
playing: bool


def main() -> None:
    """This is the main function."""
    global points
    global playing
    playing = True
    while playing == True:
        greet()
        response: str = input(player + " do you want to quit, guess a number, or reset your score?")
        if response == "quit": 
            quit()
        if response == "guess":
            points = guess()
        if response == "reset":
            reset()


def greet() -> None:
    """This is the greeting function."""
    global player
    print("welcome to the game!")
    player = input("what is your name")
    

def quit(str) -> str:
    """This is a function that allows people to quit."""
    global playing
    confirm: str = input(player + " are you sure you want to quit? 'yes' or 'no'")
    if confirm == "yes":
        print("hope you play again soon!")
        playing = False
    if confirm == "no": 
        respond: str = input("guess or reset, then?")
        if respond == "guess":
            guess
        if respond == "reset":
            reset


def guess(points: int) -> int:
    """This function lets people guess"""
    answer: int = int(input(player + "guess a one digit number (0-9) in integer form. If you are correct you get 1 point otherwise you get 0 points"))
    import random
    right_answer: int = random.randint(0, 9)
    if answer == right_answer:
        points = points + 1
    return(points)
    

def reset(str) -> None:
    """This function lets people reset their point totals"""
    global points
    confirm: str = input(player + " are you sure you want to quit? 'yes' or 'no'")
    if confirm == "yes":
        points = 0
    if confirm == "no": 
        guess


if __name__ == "__main__":
    main()