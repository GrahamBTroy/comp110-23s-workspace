from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Return CSV File..."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in dictionary under specific header."""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]: 
    """Reformats our data, so that its a dict with column headers."""
    result: dict[str,list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
         # for each key, make a dictionary entry with all column values
         result[key] = column_values(table, key)
    return result

def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    end: dict[str,list[str]] = {}
    for x in table:
        n: int = 0
        begin: list[str] = []
        while n < N: 
            begin.append(table[x][n])
            n += 1
            if N > len(table): 
                N = len(table)
        end[x] = begin
    return end

def select(table: dict[str, list[str]], chair: list[str]) -> dict[str, list[str]]:
    end: dict[str, list[str]] = {}
    for x in chair: 
        end[x] = table[x]
    return end

def concat(table: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]: 
    end: dict[str, list[str]] = {}
    for x in table: 
        end[x] = table[x]
    for y in table2: 
       n: int = 0
       if y in end: 
            while n < len(table2[y]):
                end[y].append(table2[y][n])
                n += 1
       else: 
           end[y] = table2[y]
    return end



        


