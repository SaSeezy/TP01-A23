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
# Strassen Algorithm

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        a11 = [A[i][:n//2] for i in range(n//2)]
        a12 = [A[i][n//2:] for i in range(n//2)]
        a21 = [A[i][:n//2] for i in range(n//2, n)]
        a22 = [A[i][n//2:] for i in range(n//2, n)]
        
        b11 = [B[i][:n//2] for i in range(n//2)]
        b12 = [B[i][n//2:] for i in range(n//2)]
        b21 = [B[i][:n//2] for i in range(n//2, n)]
        b22 = [B[i][n//2:] for i in range(n//2, n)]
        
        p1 = strassen(add(a11, a22), add(b11, b22))
        p2 = strassen(add(a21, a22), b11)
        p3 = strassen(a11, sub(b12, b22))
        p4 = strassen(a22, sub(b21, b11))
        p5 = strassen(add(a11, a12), b22)
        p6 = strassen(sub(a21, a11), add(b11, b12))
        p7 = strassen(sub(a12, a22), add(b21, b22))
        
        c11 = add(sub(add(p1, p4), p5), p7)
        c12 = add(p3, p5)
        c21 = add(p2, p4)
        c22 = add(sub(add(p1, p3), p2), p6)
        
        C = [c11[i]+c12[i] for i in range(n//2)] + [c21[i]+c22[i] for i in range(n//2)]
        return C

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


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
            print(strassen(matrices[j], matrices[k]))
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