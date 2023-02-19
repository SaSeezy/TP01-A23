import time
import inst_gen

def list_matrix():
    my_list = []
    for i in range(2, 6, 1): #(-S, 5, 1)
        for j in range(10):
            filename = 'ex'+str(i)+'_'+str(j)
            print(filename)
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


#############################################################################################################################
# Strassen with threshold Algorithm

def strassen_threshold(A, B, threshold=64):
    n = len(A)
    if n <= threshold:
        return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
    else:
        # Divide the matrices into 4 sub-matrices
        a11, a12, a21, a22 = split_matrix(A)
        b11, b12, b21, b22 = split_matrix(B)

        # Calculate the 7 products using Strassen's algorithm
        p1 = strassen_threshold(add_matrix(a11, a22), add_matrix(b11, b22), threshold)
        p2 = strassen_threshold(add_matrix(a21, a22), b11, threshold)
        p3 = strassen_threshold(a11, sub_matrix(b12, b22), threshold)
        p4 = strassen_threshold(a22, sub_matrix(b21, b11), threshold)
        p5 = strassen_threshold(add_matrix(a11, a12), b22, threshold)
        p6 = strassen_threshold(sub_matrix(a21, a11), add_matrix(b11, b12), threshold)
        p7 = strassen_threshold(sub_matrix(a12, a22), add_matrix(b21, b22), threshold)

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

    counter = 0
    for j in range(9): # 3 avant
        #print(matrices[j])
        #print('j: '+str(j))
        
        for k in range(j+1, 10, 1): #range(j+1, 4, 1)
            print("j:",str(j),"->k:",str(k))
            #print(matrices[k])
            print(strassen_threshold(matrices[j], matrices[k]))
            counter += 1


    print("Nombres d'operation de cet exemplaire: ", counter)
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