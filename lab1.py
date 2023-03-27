import numpy as np

# Создание элементов матрицы
n = 3
p = 6
a = np.zeros((n,p))
x = np.zeros(n)
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(p):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Перемешивание столбцов      
def swap_columns(arr, start_column, finish_column):
    arr = np.array(arr) 
    arr[:, [start_column, finish_column]] = arr[:, [finish_column, start_column]]
    return arr

# Метод Жордана-Гаусса
def gauss_jordan(a):
    for i in range(n):
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(p):
                    a[j][k] = a[j][k] - ratio * a[i][k]    
            else:
                a[i][j] = a[i][j]/a[i][j]
    return a


# Создание таблицы с коэффициентами
k = np.array([['x1', 'x2', 'x3', 'x4', 'x5', 'b']])  


# # Зануление столбцов после преобразования Жордана
def matrix_operations(a):
    gs_matrix = gauss_jordan(a)
    gs_matrix = np.array(gs_matrix)
    gs_matrix[:,3] = gs_matrix[:,3]*int(0)
    gs_matrix[:,4] = gs_matrix[:,4]*int(0)
    gs_matrix = np.around(gs_matrix, decimals = 2)
    
    return gs_matrix

def solver_ura(matrix):
    a = matrix[:,[0,1,2]]
    b = matrix[:,[3]]
    solve = np.linalg.solve(a, b)
    
    return solve

# # Перемешиваем столбцы и применяем для каждого преобразования Жордана - получается 6 решений + 1 решение обычного без перстановок
x4 = 3
for i in range(3):
    ta = a
    ids_1 = k
    xs_1 = swap_columns(ids_1, i, x4)
    matrix_1 = swap_columns(a, i, x4)
    j1_matrix = matrix_operations(matrix_1)
    new_indices_1 = xs_1[:,[0,1,2,5]]
    new_matrix_1 = j1_matrix[:,[0,1,2,5]]
    new_indices_1 = new_indices_1[:,[0,1,2]]
    solved_matrix = solver_ura(new_matrix_1)
    
    print(new_indices_1)
    print(solved_matrix)
    
       
x5 = 4
for i in range(3):
    ka = a
    ids_2 = k
    xs_2 = swap_columns(ids_2, i, x5)
    matrix_2 = swap_columns(ka, i, x5)
    j2_matrix = matrix_operations(matrix_2)
    new_indices_2 = xs_2[:,[0,1,2,5]]
    new_matrix_2 = j2_matrix[:,[0,1,2,5]]
    new_indices_2 = new_indices_2[:,[0,1,2]]
    solve_matrix = solver_ura(new_matrix_2)
    print(new_indices_2)
    print(solve_matrix)

 # Ищем последние три решения
def three_solves(matrix, first_swap, second_swap, third_swap, forth_swap):
    matrix_7 = swap_columns(matrix, first_swap, second_swap)
    matrix_7 = swap_columns(matrix_7, third_swap, forth_swap)
    
    return matrix_7

for i in range(2):
    for j in range(1,3):
        if i == 0:
            ids = three_solves(k, i, x4, j, x5)
            matrix = three_solves(a, i, x4, j, x5)
            matrix_op = matrix_operations(matrix)
            ids2 = ids[:,[0,1,2,5]]
            new_matrix = matrix_op[:,[0,1,2,5]]
            ids2 = ids2[:,[0,1,2]]
            solve_matrix = solver_ura(new_matrix)
            print(ids2)
            print(solve_matrix)
        if i == 1:
            if j == 1:
                continue
            ids = three_solves(k, i, x4, j, x5)
            matrix = three_solves(a, i, x4, j, x5)
            matrix_op = matrix_operations(matrix)
            ids2 = ids[:,[0,1,2,5]]
            new_matrix = matrix_op[:,[0,1,2,5]]
            ids2 = ids2[:,[0,1,2]]
            solve_matrix = solver_ura(new_matrix)
            print(ids2)
