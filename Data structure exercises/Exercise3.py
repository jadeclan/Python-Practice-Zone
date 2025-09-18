"""
Exercise: column-based table
Encode the following table using a 2D list, but use inner lists to represent columns instead of rows.
Now compute the average score for each test. 
Now try it if inner lists represent rows.
  
score       0   1   2
Student 0   84  85  86
Student 1   77  78  79
Student 2   92  93  94
"""
def main():
    table = [
                [84, 77, 92, 10],
                [85, 78, 93, 25],
                [86, 79, 94, 37]
             ]
    
    sums = [sum(row) for row in table]
    for i in range(len(table)):
        print(f"The average for test {i}, was {sums[i]/len(table[i]):.1f}%")
    
    transposed_table = zip(*table)                              # zip object ceated representing the transposed list
    transposed_table = [list(row) for row in transposed_table]  # convert the zip object to a list of lists
    sums = [sum(row) for row in transposed_table]
    for i in range(len(transposed_table)):
        print(f"The average for student {i}, was {sums[i]/len(transposed_table[i]):.1f}%")    

main()