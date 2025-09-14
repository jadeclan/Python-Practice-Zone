def get_yn(prompt: str)->bool:
    """
    Prompts the user for a yes/no response.
    param prompt: The question to present to the user.
    return: True for 'y', False for 'n'
    """
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response[0] == 'y':
            return True
        elif response[0] == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def get_float(prompt: str)  -> float:
    """
    Prompts the user for a numeric response.
    param prompt: The question to present to the user.
    return value: entered by the user as a float.
    """
    done = False
    while not done:
        try:
            value = input(f"{prompt}: ")
            value = float(value)
            done = True
        except Exception as e:
            print("Invalid input. Please enter a numeric value.")
    return value

def get_int(prompt: str)  -> int:
    """
    Prompts the user for an integer response.
    param prompt: The question to present to the user.
    return value: integer value entered by the user.
    """
    done = False
    while not done:
        try:
            value = input(f"{prompt}: ")
            value = int(value)
            done = True
        except Exception as e:
            print("Invalid input. Please enter an integer value.")
    return value