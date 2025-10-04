def main():
    from user_prompts import get_float, get_int    
    from future_value import future_value

    data =[[100.00,5,2],[150.00,10,10],[5.00,15,10],[1000.00,5,12]]

    for row in data:
        rate = row[1]/100.0
        fv = future_value(row[0], rate, 1, row[2])
        print(f"${row[0]:.2f} invested for {row[2]} years at an interest rate of {row[1]}% will have a future value of ${fv:.2f}.")
main()