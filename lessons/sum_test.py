"""Unit tests for sum function"""
from sum import sum

#def test_empty() -> None:
#   assert sum([]) == 0.0

#def test_one_element() -> None: 
    #test_list: list[float] = [1.0]
    #assert sum(test_list) == 1.0

def test_many() -> None: 
   xs: list[float] = [5.0, 3.0, 8.0]
   #second_test_list: list[int] = [5, 3, 9]
    #input = 1
   assert sum(xs) == 16.0

#def test_many_with_negatives() -> None: 
#   test_list: list[float] = [1.0, -2.0, 1.0]
#   assert sum(test_list) == 0.0