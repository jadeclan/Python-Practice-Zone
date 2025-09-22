def main(): 
    keys = ['name', 'tries', 'score', 'city']
    aline = ['james', 3, 2.7, 'calgary']
    aDict = {}
    for i, item in enumerate(aline):
        aDict[keys[i]] = item 
    print(aDict)
main()