def pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

question = int(input("How many levels do you want to generate? "))
print("Pascal's triangle with", question, "levels:")
pyramid = pascal(question)
for row in pyramid:
    print(" " * (question - len(row)), *row)# loops through each row of the triangle. For each row, it prints spaces 
                                                    #first, then the numbers. len(row) counts how many numbers are in the row. 
                                                    # question - len(row) calculates how many spaces to add. Shorter rows get more spaces, 
                                                    # longer rows get fewer. 
