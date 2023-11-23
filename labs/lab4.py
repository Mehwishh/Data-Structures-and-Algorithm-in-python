#Question 2
def MatMul(A,B):
    C = [[0 for x in range(len(B[0]))] for y in range(len(A))]# List of resultant matrix(Order = Rows of A x Columns of B) initialized with 0
    for i in range(len(A)):      #i = 0 --> rows of A
        for j in range(len(B[0])):   #j = 0 --> columns of B
            for k in range(len(A[0])):   #k = 0 --> columns of A
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1,2,1],[0,1,2],[0,2,1]]
B = [[3,2],[1,0],[1,1]]
print(MatMul(A,B))
#Question 2
def MatMul(A,B):
    if len(A[0]) == len(B):      # For matrix multiplication columns of A == rows of B
        C = [[0 for x in range(len(B[0]))] for y in range(len(A))] # List of resultant matrix (Order = Rows of A x Columns of B) initialized with 0
        for i in range(len(A)):      # i = 0 --> rows of A
            for j in range(len(B[0])):   # j = 0 --> columns of B
                for k in range(len(A[0])):   # k = 0 --> columns of A
                    C[i][j] += A[i][k] * B[k][j]
        return C
    else:
        return "Given Matrices are not conformable for Multiplication!!"
A = [[1,2],[1,2],[2,1]]
B = [[3,2,0]]
print(MatMul(A,B))
