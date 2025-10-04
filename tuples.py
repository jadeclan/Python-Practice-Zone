def main():
    my_tuple = (1, 2, (3,4,5), ['a','b','c'],'hello world')

    print(my_tuple)
    
    # my_tuple[0] = 7           -> This failed due to type error
    # my_tuple[2].append('d')   -> a tuple is immutable so you can't change it's contents. tuples don't have append method.
    # my_tuple[3].append('d')   -> This works because a list is mutable.
    # my_tuple[4].append('!')   -> String object does not have an append method
    # my_tuple[4] += '!'        -> tuples don't support assignment
    my_list = list(my_tuple)    # Cast the tuple to a list first
    my_list[4] += "!"           # type: ignore
    my_tuple = tuple(my_list)   # Cast the list back to a tuple, overiding the original.
    print(f"{my_tuple[4]}")
    print(f"Modified tuple now contains: {my_tuple}")
main()