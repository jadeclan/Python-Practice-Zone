def main():
    done = False
    while not done:
        cash_required = input("Enter the cash required(include $): ")
        if cash_required.startswith('$'):
            cash_required = cash_required[1:]
            try :
                cash_required = float(cash_required)
                print(f"Cash required is: $ {cash_required:.2f}")
                done = True
            except:
                print("Invalid input. Please enter a valid amount.")
        else:
            print("Invalid input. Please start with '$'.")
    
    done = False
    while not done:
        people = input("Enter the number of people sharing the prize: ")
        try:
            people = int(people)
            if people > 0:
                cash_per_person = int((cash_required / people)*100)/100
                print(f"Each person should get: $ {cash_per_person:.2f}")
                done = True
            else:
                print("Number of people must be greater than zero.")
        except:
            print("Invalid input. Please enter a valid number of people.")
    
    print(f"There was $ {cash_required-people*cash_per_person:.2f} not shared among the {people} people.")
        
    
main()