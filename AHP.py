from functions import *
import numpy as np
import sys
import matplotlib.pyplot as plt

# Input Multiple matrices
file = open('file.txt').read() #Open the File
matrix_list = file.split("\n\n") #Split the file in a list of Matrices
for i, m in enumerate(matrix_list): 
    matrix_list[i]=m.split("\n") #Split the row of each matrix
    for j, r in enumerate(matrix_list[i]): 
        matrix_list[i][j] = r.split() #Split the value of each row


matrices = len(matrix_list) - 1

over_all = []
percentage = []
for i in range(matrices):
    oa = []
    R = len(matrix_list[i][0])
    # Inserting each matrix
    matrix = matrix_list[i]
    # Calculate Si
    Si = []
    for i in range(R):
        b: int = 0
        for j in range(R):
            b += float(matrix[j][i])
        Si.append(b)
    for i in range(R):
        print(f'S{i + 1}= {Si[i]}')

    # Calculate eigenvector Wi
    Wi = []
    Norm = []
    for i in range(R):
        c = []
        for j in range(R):
            k = float(matrix[i][j]) / float(Si[j])
            c.append(k)
        Norm.append(c)

    z = []
    for i in range(R):
        d: float = 0
        for j in range(R):
            d += Norm[i][j]
        z.append(d)
    print(z)

    for i in range(R):
        k = z[i] / float(R)
        Wi.append(k)
        oa.append(k)
    over_all.append(oa)

    for i in range(R):
        print(f'W{i + 1}= {Wi[i]}')
    # Calculate lambda

    lambda_max: float = 0
    for i in range(R):
        lambda_max += Si[i] * Wi[i]
    print("lambda = ", lambda_max)
    # Calculate Consistency indicies

    consistency_indicies = (lambda_max - R) / (R - 1)
    print("consistency indicies = ", consistency_indicies)
    # Calculate Consistency Ration
    ri = [0, 0, 0.0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.51]
    print(ri[R])
    consistency_ratio = consistency_indicies / ri[R]
    print("consistency Ratio = ", consistency_ratio)


R = (len(matrix_list[0][1]))
for i in range (R):
    s: float = 0
    for j in range (matrices):
        s += over_all[j][i]
    avr = s / matrices
    percentage.append(avr)


labels = []

for i in range(R):
    t = i + 1
    labels.append("C"+str(t))



fig1, ax1 = plt.subplots()
ax1.pie(percentage, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()






