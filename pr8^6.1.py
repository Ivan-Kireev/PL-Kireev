matrix = [
    [3, 8, 5],
    [1, 6, 9],
    [4, 7, 2]
]
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
print("Наибольшие элементы в каждой строке:", max_in_rows)
print("Наименьшие элементы в каждом столбце:", min_in_columns)
