from typing import Counter
import numpy as np
import itertools
import math

def read(message):
    # reading input(try-catch)
    try:
        matrix_size = int(input(message))
        if(matrix_size <= 0): raise TypeError
    except TypeError: 
        print("Input should be integer, more than 0") 
        return 0
    return matrix_size
    
def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

    
def matrix_permutation(matrix, matrix_size):
    #Finding all possible permutations of n elements of matrix 
    matrix_indexs_permutated = [ i for i in range(matrix_size)]
    index_permutation = list(itertools.permutations(matrix_indexs_permutated, matrix_size))
    temp_permutation_list = []
    matrix_permutation = []
    index = []
    for i in range(0, math.factorial(matrix_size)):
        for j in range(0, (matrix_size)):
            temp_permutation_list.extend([matrix[j][index_permutation[i][j]]])
        matrix_permutation.append(temp_permutation_list)
        temp_permutation_list = []
    return matrix_permutation

def multiplication(matrix_permutation):
        #Finding multiplication of set of n elements
    multiplication = []
    for permutation_list in matrix_permutation:
        temp = 1
        for x in permutation_list:
            temp *= x
        multiplication.append(temp)
    return multiplication
def sum(multiplication):
 #Finding sum if multiplication, considering sign(n)
    res = 0
    counter = 0
    index = 0
    index_permutation = list(itertools.permutations([ i for i in range(matrix_size)], matrix_size))
    for index_list in index_permutation:
        counter = 0
        #Finding inversion(bubble sort)
        for i in range(matrix_size):
            for j in range(i+1, matrix_size):
                if index_list[i] > index_list[j] :
                    counter += 1
        if(counter % 2 == 0): res += multiplication[index] 
        else: res -= multiplication[index]
        index += 1
    return res


def find_determinant(matrix, matrix_size):
    #Composition, finding determinant of matrix
    return sum(multiplication(matrix_permutation(matrix, matrix_size)))

    

matrix_size = read("Input size of your matrix: ")
matrix = random_matrix(matrix_size)
print("Your matrix is: ")
print(matrix)
print("My Det = " + str(find_determinant(matrix, matrix_size)))
print("Correct Der = " + str(np.linalg.det(matrix)))