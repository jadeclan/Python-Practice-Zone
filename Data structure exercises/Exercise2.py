"""
Exercise: deleting even-numbered list items
Write a function that accepts a list, and deletes all the even-numbered items from the list.
So the list	['a', 'b', 'c', 'd'
becomes	['b','d']
"""
def main():
    # deleting using del keyword
    mylist = [1,2,3,4,5,6,7,8,9]
    newlist = []
    for i in range(len(mylist)-1,-1,-1):    # using range() with start, stop, step
        if mylist[i]%2 == 0:
            del mylist[i]
    print(f"Expecting [1, 3, 5, 7, 9]. Got: {mylist}")

    # deleting using list comprehension
    mylist = [1,2,3,4,5,6,7,8,9]
    mylist = [mylist[i] for i in range(len(mylist)) if mylist[i]%2 != 0]
    print(f"Expecting [1, 3, 5, 7, 9]. Got: {mylist}")

    # to delete odd index items in a list
    mylist = [1,2,3,4,5,6,7,8,9]
    newlist = []
    for i in range(len(mylist)):
        if i%2 == 0:
            newlist.append(mylist[i])
    print(f"Expecting [1, 3, 5, 7, 9].  Got: {newlist}")

    # Putting the above for-if structrute into a list comprehension
    mylist = ['a','b','c','d']
    newlist = [mylist[i] for i in range(len(mylist)) if i%2 != 0]
    print(f"Expecting ['b', 'd'].  Got: {newlist}")
main()