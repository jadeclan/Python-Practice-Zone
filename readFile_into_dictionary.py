def check_value(value) -> bool:
    try:
        value = float(value)
        return True
    except:
     return False   

filename = 'test.txt'
data = []
lines = []
try:
    with open(filename,'r') as file:
        for line in file:
            lines.append(line)
    # Read first and parse into a list of headers
        headers = lines[0].split(',')
        header_keys = []
        for col in headers:
            col = col.strip()
            header_keys.append(col)

        for line in lines[1:]:
            this_row = line.split(',')
            scrubbed_dictionary = {}
            # No casting to float, column data type checking, or equal col 
            # length checking.
            for i, item in enumerate(this_row):
                item = item.strip()
                try:
                    item = float(item)
                    scrubbed_dictionary[header_keys[i]] = item
                except:
                    scrubbed_dictionary[header_keys[i]] = item
            data.append(scrubbed_dictionary)
except:
    raise FileNotFoundError('Input file not found.') 

print(data)

filename = 'test.json'
with open(filename, 'w') as file:
    for i, line in enumerate(data):
        if i == 0:
            file.write(f'{{"{str(i)}":{{')
        else:
            file.write(f'"{str(i)}":{{')
        if i != len(data)-1:
            for j, (key, value) in enumerate(line.items()):
                if j != len(line)-1:
                    if check_value(value):
                        file.write(f'"{key}":{value},')
                    else:
                        file.write(f'"{key}":"{value}",')
                else:
                    if check_value(value):
                        file.write(f'"{key}":{value} }},')
                    else:
                        file.write(f'"{key}":"{value}" }},')
        else:
            for j, (key, value) in enumerate(line.items()):
                if j != len(line)-1:
                    if check_value(value):
                        file.write(f'"{key}":{value},')
                    else:
                        file.write(f'"{key}":"{value}",')
                else:
                    if check_value(value):
                        file.write(f'"{key}":{value} }}')
                    else:
                        file.write(f'"{key}":"{value}" }}')
            file.write('}') 

# Test to see if the json file will open using json library
import json
with open('test.json', 'r') as file:
    data = json.load(file)
print(data)