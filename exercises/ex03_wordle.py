"""EX03 - Structured Wordle"""
__author__ = "730561058"
count: int = 0
def contains_char(inputed_word: str, inputed_letter: str)-> bool:
  assert len(inputed_letter) == 1
  while count <= len(inputed_letter):
   count = count + 1
   if inputed_letter == inputed_word[count]: 
       return True
   else:
       return False

# setting up variables
