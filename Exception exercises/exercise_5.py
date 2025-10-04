def get_yn(prompt: str)->bool:
    """
    Prompts the user for a yes/no response and returns True for 'y' and False for 'n'.
    """
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response[0] == 'y':
            return True
        elif response[0] == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
def nested_if_demo():
    """
    Demonstrates nested if statements to determine loan eligibility.
    """
    good_credit = get_yn("Does applicant have good credit?")
    if good_credit:
        salary_threshold = get_yn("Is the applicant's salary above $30,000?")
        if salary_threshold:
            age_threshold = get_yn("Is the applicant's over 30 years old?")
            if age_threshold:
                print("Applicant is eligible for a $10,000 loan.")
            else:
                print("Applicant is eligible for a $5,000 loan.")
        else:
            print("Applicant is ineligible for a $1,000 loan.")
    else:
        print("Applicant is ineligible for a loan.")

def if_elif_demo():
    """
    Demonstrates if-elif statements to determine loan eligibility.
    """
    good_credit = get_yn("Does applicant have good credit?")
    salary_threshold = get_yn("Is the applicant's salary above $30,000?")
    age_threshold = get_yn("Is the applicant's over 30 years old?")
    if not good_credit:
        print("Applicant is ineligible for a loan.")
    elif not salary_threshold:
        print("Applicant is eligible for a $1,000 loan.")
    elif not age_threshold:
        print("Applicant is eligible for a $5,000 loan.")
    else:
        print("Applicant is eligible for a $10,000 loan.")  

def main():
    while True:
        # nested_if_demo()
        if_elif_demo()           
        quit = get_yn("Do you want to run another check? \n If no, the program will terminate.")
        if quit == False:
            print("Program terminated.")
            break
main()