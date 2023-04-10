"""Example function for unit tests"""
def sum(xs: list[int]) -> int:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    #while idx <= len(xs) - 1:
    #    sum_total += xs[idx]
    #    idx += 1
    # return sum_total
    for num in range(0, len(xs)): 
        sum_total += xs[num]
    return sum_total
      
