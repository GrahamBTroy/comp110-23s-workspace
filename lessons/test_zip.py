from lessons.zip import zip

def test_zip() -> None: 
    keys: list[str] = ["a", "b", "c", "d", "e"]
    values: list[str] = [1, 2, 3, 4, 5]
    assert zip(keys, values) == {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5}
