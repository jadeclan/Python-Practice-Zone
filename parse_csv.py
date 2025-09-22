def main():
    filename = 'census_dataset.txt'
    delimeter = ','
    file_contents = []

    with open(filename,'r') as file:
        for line in file:
            line = parse_row(line, delimeter)
            file_contents.append(line)
    
    for line in file_contents:
        print(f'{line[0]}\t{line[1]:.6}\t{line[2]}\t{line[3]:.6}\t')


def parse_row(row: str, delimeter: chr) -> list:
    """Function that parses a row using the split method.
    Args:
        row (str): a string of data that needs to be parsed
        delimeter (chr): the character to use to parse the data on
    Returns:
        list: a list containing the column representation of the input string.
    """    
    items = []
    parsed_row = row.split(delimeter)

    for column in parsed_row:
        column = column.strip()
        items.append(column)
    return items

main()    