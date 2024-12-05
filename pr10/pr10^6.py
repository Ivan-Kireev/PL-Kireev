def read_matrix_from_file(KIREEV_IVAN_UB41_VVOD):
    with open(KIREEV_IVAN_UB41_VVOD, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def write_results_to_file(KIREEV_IVAN_UB41_ViVOD, max_in_rows, min_in_columns):
    with open(KIREEV_IVAN_UB41_ViVOD, 'w') as file:
        file.write("Наибольшие элементы в каждой строке: " + str(max_in_rows) + "\n")
        file.write("Наименьшие элементы в каждом столбце: " + str(min_in_columns) + "\n")

matrix = read_matrix_from_file('KIREEV_IVAN_UB41_VVOD.txt')
num_rows = len(matrix)
num_columns = len(matrix[0])

max_in_rows = []
for i in range(num_rows):
    max_element = matrix[i][0]
    for j in range(1, num_columns):
        if matrix[i][j] > max_element:
            max_element = matrix[i][j]
    max_in_rows.append(max_element)

min_in_columns = []
for j in range(num_columns):
    min_element = matrix[0][j]
    for i in range(1, num_rows):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
    min_in_columns.append(min_element)


write_results_to_file('KIREEV_IVAN_UB41_ViVOD.txt', max_in_rows, min_in_columns)
