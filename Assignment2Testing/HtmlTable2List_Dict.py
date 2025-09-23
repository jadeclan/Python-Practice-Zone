def load_file(filename: str) -> list:
    """Putting file to be read into a list for further processing.
    Args:
        filename (str): The file (including path) to be read
    Returns:
        list: A list containing each line of the file as text
    Raises:
        FileNotFoundError: Unable to read file.
        EmptyFileError: The file opened contained no contents.
    """    
    lines = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []    
    return lines

def load_from_html(file_contents: list) -> list[dict]:
    """Reads a dataset that is in likely in HTML format. Converts numeric data 
    to float. Raises an AttributeError if the table rows do not all have the 
    same number of values.
    Args:
        filename (str): The file name (with path) of the html data to read
    Returns:
        list[dict]: Return the dataset as a list of dictionaries - one dict per
                    object in the file. Each dictionary should map column names
                    to values
    Raises:
        NotImplementedError: CSV file contains format errors
    """    
    # Find <tr>, <td>, </td> and </tr> tags and put into a list
    return_list = []
    cntr = 1
    for line in file_contents:
        line = line.strip().lower()
        if cntr >= 5:
            break
        if '<tr>' in line:
            list_item = ''
        if '<td>' in line:
            # this is a column value:
            col_data = strip_tags(line)
            list_item = list_item + col_data + ','
        if '</tr>' in line:
            # this is the end of a dictionary item, remove last comma and close 
            # the dict
            list_item = list_item[:-1] + ''
            return_list.append(list_item)
            cntr += 1
            print(list_item[:30])  # Print first 30 characters of the list item for debugging

    return_list = list_to_list_of_dicts(return_list)  
    return return_list

def strip_tags(line: str) -> str:
    """Strips HTML tags from a line and returns the content.
    Args:
        line (str): A line of HTML text
    Returns:
        str: The content of the line without HTML tags
    """
    for tag in ['<tr>', '</tr>', '<td>', '</td>']:
        line = line.replace(tag, '').strip()
    return line 

def list_to_list_of_dicts(data: list) -> list[dict]:
    
    header = data[0]
    return_list = []
    for line in data:
        if line != header:
            line = convert2dict(line, header)
            return_list.append(line)
    return return_list

def convert2dict(line: list, keys: list) -> dict:
    """Convert a validated, consistent, well formatted list row into a 
       dictionary
    Args:
        line (list): A line in list format that needs to be converted to 
                     dictionary format
        keys (list): Keys to associate the values in the line variable with.
    Returns:
        dict: A dictionary representation of the list formatted item that was 
        input.
    """    
    this_item = {}
    for i, item in enumerate(line):
        this_item[keys[i]] = item 
    return this_item

def main():
    """Main function to run the program."""
    filename = "Assignment2Testing\student_dataset.txt" 
    file_contents = load_file(filename)
    if file_contents:
        print(f"Successfully loaded {len(file_contents)} lines from {filename}.")
        # Further processing can be done here
    else:
        print("Failed to load lines from the file.")

    if '<table>' in file_contents[0].strip().lower():
        # We now have a html file, let's try to handle it.
        return_list = load_from_html(file_contents)

main()