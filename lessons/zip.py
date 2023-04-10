def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    end: dict[str, int] = {}
    if len(keys) != len(values): 
        return end
    
    i: int = 0
    while i < len(keys):
        end[keys[i]] = values[i]
        i += 1
    return end
