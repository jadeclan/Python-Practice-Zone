    
def main():
    import json
    filename = 'test.json'
    data = [
        {"key1": 1, "key2": 20.1, "key3": "james"},
        {"key1": 2, "key2": 20.2, "key3": "fred"},
        {"key1": 3, "key2": 20.3, "key3": "george"},
        {"key1": 4, "key2": 20.4, "key3": "something"}
    ]

    print(data)

    with open(filename, "w") as f: 
        f.write('{\n')
        for i, row in enumerate(data):
            last_key = list(row.keys())[-1]
            parts = f'"row{i}":{{'
            for key in row:
                if not isinstance(key, str):
                    raise TypeError("Dictionary keys must be strings for JSON serialization.")
                string_key = f'"{key}"'
                if isinstance(row[key], str):
                    value = f'"{row[key]}"'
                elif (isinstance(row[key],float) or isinstance(row[key],int)):
                    value = str(row[key])
                else:
                    raise TypeError("Dictionary values must be strings, floats or integers")
                parts += string_key + ':' + value
                if key != last_key:
                    parts = parts + ','
                else:
                    parts = parts + '}'
            if row != data[-1]:
                f.write(f"{parts},\n")
            else:
                f.write(f"{parts} \n")
        f.write('}')
    f.close()

    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            print(data)
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from 'your_file.json'. Check file format.")

main()