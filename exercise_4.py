def get_float(prompt: str)  -> float:
    """
    Prompt the user for a floating-point value.
    param prompt: the prompt to display to the user
    return: the floating-point value entered by the user
    """
    done = False
    while not done:
        try:
            pv = input(f"{prompt}: ")
            pv = float(pv)
            done = True
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return pv

def get_int(prompt: str)  -> int:
    """
    Prompt the user for an integer value.
    param prompt: the prompt to display to the user
    return: the integer value entered by the user
    """
    done = False
    while not done:
        try:
            n = input(f"{prompt}: ")
            n = int(n)
            done = True
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    return n

def future_value(pv: float, r: float, n: int, t: float) -> float:
    """
    Calculate the future value of an investment.
    param pv: present value
    param r: annual interest rate (as a decimal)
    param n: number of times interest is compounded per year
    param t: number of years the money is invested
    return: future value
    """
    return pv * (1 + r/n)**(n*t)

def main():

    pv = get_float("Enter the present value")
    r = get_float("Enter the annual interest rate (as a decimal)")
    n = get_int("Enter the number of times interest is compounded per year")
    t = get_float("Enter the number of years the money is invested")
    fv = future_value(pv,r,n,t)

    print(f"In {t} years, your investment of ${pv:.2f} will be worth ${fv:.2f}")

main()