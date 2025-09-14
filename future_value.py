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