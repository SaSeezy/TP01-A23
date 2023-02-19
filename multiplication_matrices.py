import time
import inst_gen

def list_matrix():
    my_list = []
    for i in range(2, 6, 1): #(-S, 5, 1)
        for j in range(10):
            filename = 'ex'+str(i)+'_'+str(j)
            print(filename) # Affichage des noms de differents fichiers obtenus
            mat = []  
            with open(filename, 'r') as file:
                """lines = file.readlines()
                print(lines)"""
                start_line = 0
                for k, line in enumerate(file):
                    if k > start_line:
                        #print(line)
                        line = line.split()
                        if line:
                            row = [int(x) for x in line]
                            #print(row)
                            mat.append(row)
            my_list.append(mat)
    return my_list

#print(list_matrix())

#for i in my_list:
    #print(i)

def multiply_matrices(matrix1, matrix2):
    #start = time.time()

    # Get the number of rows and columns of the matrices
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    print(cols1)
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    print(cols2)

    # Check if the matrices can be multiplied
    if cols1 != rows2:
        return "Error: The number of columns of the first matrix must be equal to the number of rows of the second matrix."

    # Initialize the result matrix with zeros
    result = [[0 for col in range(cols2)] for row in range(rows1)]

    # Perform the matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
    
    #end = time.time()
    #print("Temps d'execution de la matrice: ", (end - start)* 10**3, " ms")

    return result



# List of merged matrices in different files
my_list = list_matrix()

# Liste des temps d'execution
time_list = []

index = 1
#start = time.time()
# Matrices multiplication based on conventional method
for i in range(0, 40, 10): #(0, nb_tailles*nb_exemplaires, nb_exemplaires)

    # This line is to gathered matrices with similar row and col(corresponding to NB_EXEMPLAIRES) 
    matrices = my_list[i:i+10] # 4 avant

    # Calcul du temps d'un exemplaire
    start = time.time()
    #print(multiply_matrices(matrices[0], matrices[1]))

    for j in range(9):
        #print(matrices[j])
        #print('j: '+str(j))
       
        for k in range(j+1, 10, 1): 
            print("j:",str(j),"->k:",str(k))
            #print(matrices[k])
            print(multiply_matrices(matrices[j], matrices[k]))


    temps_exec = (time.time() - start)* 10**3
    time_list.append(temps_exec)
    print("Temps d'execution des matrices de l'exemplaire ",index, ":", temps_exec, " ms")
    index = index + 1
    print(' ')

print("Liste des temps d'execution en microsecondes:", time_list)
#end = time.time()
#print("Temps d'execution des matrice de tout:", (end - start)* 10**3, " ms")


# Calcul du temps d'execution moyen des exemplaires
sum = 0
for temps in time_list:
    sum =+ temps

temps_moyen = sum/len(time_list)
print("Temps d'execution moyen en microsecondes:", temps_moyen)


"""
## Strassen with threshold

def matrix_mult(A, B, threshold=64):
    n = len(A)
    if n <= threshold:
        return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
    else:
        # Divide the matrices into 4 sub-matrices
        a11, a12, a21, a22 = split_matrix(A)
        b11, b12, b21, b22 = split_matrix(B)

        # Calculate the 7 products using Strassen's algorithm
        p1 = matrix_mult(add_matrix(a11, a22), add_matrix(b11, b22), threshold)
        p2 = matrix_mult(add_matrix(a21, a22), b11, threshold)
        p3 = matrix_mult(a11, sub_matrix(b12, b22), threshold)
        p4 = matrix_mult(a22, sub_matrix(b21, b11), threshold)
        p5 = matrix_mult(add_matrix(a11, a12), b22, threshold)
        p6 = matrix_mult(sub_matrix(a21, a11), add_matrix(b11, b12), threshold)
        p7 = matrix_mult(sub_matrix(a12, a22), add_matrix(b21, b22), threshold)

        # Calculate the 4 sub-matrices of the result
        c11 = add_matrix(sub_matrix(add_matrix(p1, p4), p5), p7)
        c12 = add_matrix(p3, p5)
        c21 = add_matrix(p2, p4)
        c22 = add_matrix(sub_matrix(add_matrix(p1, p3), p2), p6)

        # Combine the sub-matrices to form the result
        return join_matrix(c11, c12, c21, c22)

def split_matrix(matrix):
    n = len(matrix) // 2
    return (matrix[:n][:n], matrix[:n][n:], matrix[n:][:n], matrix[n:][n:])

def add_matrix(A, B):
    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(A, B)]

def sub_matrix(A, B):
    return [[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(A, B)]

def join_matrix(A, B, C, D):
    return [row1 + row2 for row1, row2 in zip(A, C)] + [row1 + row2 for row1, row2 in zip(B, D)]


"""