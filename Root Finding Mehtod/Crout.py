import numpy as np

# one-liner logic to take input for rows and columns 
#A = [[int(input()) for x in range (3)] for y in range(3)]

def crout(A):

    L = np.zeros((3, 3))
    U = np.zeros((3, 3))

    for k in range(0, 3):
        U[k, k] = 1 

        for j in range(k, 3):
            sum0 = sum([L[j, s] * U[s, k] for s in range(0, j)]) #range from index 0
            L[j, k] = A[j, k] - sum0 #reversed index

        for j in range(k+1, 3):
            sum1 = sum([L[k, s] * U[s, j] for s in range(0, k)]) #range from index 0
            U[k, j] = (A[k, j] - sum1) / L[k, k]



    print(L)
    print()
    print(U)
    return L, U


A = np.array([[2, 1, 1], [3, 2, 3], [1, 4, 4]])
crout(A)