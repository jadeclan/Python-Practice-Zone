def main():
    seq = [(1,2,3),(4,5,6),(7,8,9)]
    for a, b, c in seq:
        print(f"a={a}, b={b}, c={c}")
        print('a={a}, b={b}, c={c}'.format(a=a, b=b, c=c))


main()