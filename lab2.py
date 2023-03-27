import numpy as np
def swap_columns(arr, start_column, finish_column):
    arr = np.array(arr) 
    arr[:, [start_column, finish_column]] = arr[:, [finish_column, start_column]]
    return arr

a = np.array([[7,2,3,7,2,21], [-3,-2,-6,6,-8,-13], [0,1,-2,-1,4,2]])
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        if a[i][5] < 0:
            a[i][j] = a[i][j]*int(-1)
        else:
            a[i][j] = a[i][j]

            L = np.array([[-1,0,-6,9,0,0]])
def Ll(L):
    l = []
    for elem in L:
        for x in elem:
            if x != 0:
                x = int(x*(-1))
            else:
                x = int(x)
            l.append(x)
    L = np.array(l)
    return L

L = Ll(L)

# Введение вспомогательной функции L
for elem in a:
    vspmg = int(-1)*(a[0] + a[1] + a[2])
vspmg = np.hstack([vspmg, np.array([0,0,0])])   
# Приведение к искусственному базису
gauss_matrix = np.array([[1,0,0],[0,1,0],[0,0,1]])
A = np.hstack([a, gauss_matrix])
L = np.hstack([L, np.array([0,0,0])])
vs = np.vstack([A, L, vspmg])
vs = swap_columns(vs, 5, 8)
vs = vs.astype('float')

# Поиск наименьшего элемента в строке
def min_col(matrix):
    min_elem = 0
    index_min_elem = -1
    matrix = matrix[4, :5]
    for i in range(len(matrix)):
        if matrix[i] < min_elem:
            min_elem = matrix[i]
            index_min_elem = i
    return index_min_elem

# Посик наименьшего элемента в соотношении столбцов
def min_row(matrix, k):
    matrix = vs[:3][:,8]
    small_matrix = vs[:3][:,k]
    result = matrix/small_matrix
    min_elem = result[0]
    index_min_elem = 0
    for i in range(len(result)):
        if result[i] < min_elem:
            min_elem = result[i]
            index_min_elem = i
    return index_min_elem

iter_1 = vs.copy()
k = 2
p = 4
for i in range(5):
    for j in range(9):
        if i == k:
            iter_1[i][j]= vs[i][j]/vs[k][p]
        elif j == p:
            iter_1[i][j] = 0
        else:
            iter_1[i][j] = vs[i][j] - (vs[i][p]*vs[k][j])/vs[k][p]
for i in range(0, len(iter_1)):
    for j in range(0, len(iter_1[i])):
        iter_1[i][j] = np.around(iter_1[i][j], decimals=3) 
print(iter_1)

k = 1
p = 2
iter_2 = iter_1.copy()
for i in range(5):
    for j in range(9):
        if i == k:
            iter_2[i][j]= iter_1[i][j]/iter_1[k][p]
        elif j == p:
            iter_2[i][j] = 0
        else:
            iter_2[i][j] = iter_1[i][j] - (iter_1[i][p]*iter_1[k][j])/iter_1[k][p]
for i in range(0, len(iter_2)):
    for j in range(0, len(iter_2[i])):
        iter_2[i][j] = np.around(iter_2[i][j], decimals=3) 
print('\n')
print(iter_2)

iter_3 = iter_2.copy()

k = 0
p = 3
for i in range(5):
    for j in range(9):
        if i == k:
            iter_3[i][j]= iter_2[i][j]/iter_2[k][p]
        elif j == p:
            iter_3[i][j] = 0
        else:
            iter_3[i][j] = iter_2[i][j] - (iter_2[i][p]*iter_2[k][j])/iter_2[k][p]
for i in range(0, len(iter_3)):
    for j in range(0, len(iter_3[i])):
        iter_3[i][j] = np.around(iter_3[i][j], decimals=3) 
print('\n')
print(iter_3)
print('\n')

# Решение основной задачи симплекс-метода
print("Опорный план найден!")
simplex_table_1 = iter_3[0:4]
print(simplex_table_1)

