months =['jan','feb','mar','apr']
numbers =[1,2,3,4]

def get_month_number(month_name: str) -> int:
    for i in range(len(months)):
        if months[i] == month_name:
            return numbers[i]
        return -1
months_dict = {'jan':1,'feb':2,'mar':3,'apr':4}
def get_month_from_dict(month_name: str) -> int:
    if month_name not in months_dict:
        return -1
    return months_dict[month_name]

month = 'dec'
answer1 = get_month_number(month)
answer2 = get_month_from_dict(month)
print(f"{answer1} and {answer2}")
    