def main():
    months = ('January', 'February', 'March', 'April', 
              'May', 'June', 'July', 'August', 'September', 
              'October', 'November', 'December')
    data = ('2024-10-03','AAPL',100.02,-2.3)
    
    # Unpack the data tuple into individual variables
    year = int(data[0][:4])
    month = int(data[0][5:7])
    day = int(data[0][9:])
    print(f"On {months[month-1]} {day}, {year}, {data[1]}'s stock closed at $ {data[2]}.")
main()