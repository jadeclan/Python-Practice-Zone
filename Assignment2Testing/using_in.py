def main():
    # simple list to be used to practice searching lists
    file_contents = [
        ["the nice thing", 'about a list', "is unkown"],
        ["this is","testing some","functionality"]
    ]
    file_contents1 = [
        ['the nice thing about a list is unkown'],
        ['this is testing some functionality']
    ]
    file_contents2 = ['the nice thing about a list, is unkown',
                     'this is testing some functionality']

    # result and result1 fail because we have a 2d list
    result = ',' in file_contents
    print (f", in file_contents is {result}")

    result1 = ',' in file_contents1
    print (f", in file_contents1 is {result1}")

    result2 = (',' in file_contents2)
    print (f", in file_contents2 is {result2}")

    result3 = any(',' in line for line in file_contents2)
    print (f", in file_contents2 is {result3}") 

    for line in file_contents2:
        print (line)
        if ',' in line:
            print ("TRUE")
        else:
            print("FALSE")

    # line 24-5 provides the functionality of lines 27-32
main()