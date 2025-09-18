"""
Exercise: modifying list contents
Write a function that increments each item in a list by one.
i.e. passing the list [0, 1, 2, 3, 4] should return the list [1, 2, 3, 4, 5]
Your function should not modify the list that was passed in.

"""
def main():
    mylist = [0,1,2,3,4]

    for i in range(len(mylist)):
        mylist[i] += 1

    print(f"Expecting [1, 2, 3, 4, 5], got: {mylist}")

main()