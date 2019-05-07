def matrix_addition(a,b):
    for row in range(len(a)):
        for col in range(len(a[0])):
            a[row][col] += b[row][col]

    return a

print(matrix_addition([ [1, 2],[1, 2] ], [ [2, 3],[2, 3] ]))
