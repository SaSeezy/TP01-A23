import time
import csv

header = ['Fichier','Taille matrice (n)', 'Temps d\'excution(y)']
                
#list_data = []
data = []
data.append(header)
#list_data.append(data)

def list_matrix():
    for i in range(2, 6, 1): #(-S, 5, 1)
        for j in range(10):
            filename = 'ex'+str(i)+'_'+str(j)
            print(filename)
            mat = []
            start = time.time()  
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
            
            print(len(mat[0]))
            temps_exec = (time.time() - start)* 10**3
            ligne = [filename, len(mat[0]), temps_exec]
            data.append(ligne)
    
        print("Temps d'execution:", temps_exec, " ms")

    #list_data.append(data)
    return data


donnee = list_matrix()
print(donnee)

filename = "data.csv"

# finding the maximum width of each column
widths = len(donnee[0][2])



# writing to CSV file
with open(filename, 'w', newline='') as csvfile:
    #csvwriter = csv.writer(csvfile,  delimiter=',')
    csvwriter = csv.writer(csvfile)
    for row in donnee:
        row = [str(cell).ljust(widths) for i, cell in enumerate(row)]
        csvwriter.writerow(row)

print(f"CSV file '{filename}' created successfully")