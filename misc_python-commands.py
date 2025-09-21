def main():
    seq = [(1,2,3),(4,5,6),(7,8,9)]
    """
    for a, b, c in seq:
        print(f"a={a}, b={b}, c={c}")
        print('a={a}, b={b}, c={c}'.format(a=a, b=b, c=c))
    """
    this_list = list(range(5))
    #print(this_list, len(this_list))

    a = 2
    b = a
    # print(id(a),id(b))  # same memory location
    b = b + 2
    # print(id(a),id(b))   # different memory locations

    """
    num = 5
    print('line 2:', f'num={num}', f'id={id(num)}')

    def modify_a_number(num: int) -> None:
        print('line 5:', f'num={num}', f'id={id(num)}')
        num = num + 1
        print('line 7:', f'num={num}', f'id={id(num)}')
        print(num)

    modify_a_number(num)  # prints 6
    print('line 10:', f'num={num}', f'id={id(num)}')
    print(num)  # prints 5
    """
    strings = {
        'january': 1,
        'february': 2,
        'march': 3,
        'fe': 4
    }
    string_lengths = {s: len(s) for s in strings}
    print(string_lengths)
    string_lengths_more_than_2 = {s: len(s) for s in strings if len(s) > 2}
    print(string_lengths_more_than_2)

main()