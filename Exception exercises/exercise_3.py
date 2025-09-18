def main():
    test_data = "Suppose the word 'Eric' is now considered offensive." + \
                "Write a program that will take a string and check if it contains the word 'Eric'" + \
                "(with any capitalization: 'Eric', 'eric', 'ERIC', 'eRiC', etc.). Can you make your program" + \
                "remove the word? will your program also remove the word 'tumeric'?"
    lower_test_data = test_data.lower()
    lower_test_data = lower_test_data.replace(' eric ', '')
    lower_test_data = lower_test_data.replace("'eric'", "''")
    print(lower_test_data)   

main()