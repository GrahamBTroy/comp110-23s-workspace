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

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
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
         result[key] = column_vals(table, key)
    return result
