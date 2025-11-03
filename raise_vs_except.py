numb = 0

try:
    ratio = 10 / numb

# Note: Once the error message is printed the program continues to execute
except ZeroDivisionError:
    print('this is line 8')
    
numb = -2.
# Note: the program execution pauses when the exception is raised.
if numb <= 0: 
    raise ZeroDivisionError('This is line 10')
