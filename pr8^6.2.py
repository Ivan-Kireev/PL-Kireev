N = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

max_value = float('-inf')
max_position = (-1, -1)
n = N // 2
for i in range(N):
    main_diag_value = matrix[i][i]
    if main_diag_value > max_value:
        max_value = main_diag_value
        max_position = (i, i)

    secondary_diag_value = matrix[i][N - 1 - i]
    if secondary_diag_value > max_value:
        max_value = secondary_diag_value
        max_position = (i, N - 1 - i)

center_value = matrix[n][n]
center_position = (n, n)

matrix[max_position[0]][max_position[1]], matrix[center_position[0]][center_position[1]] = (
    center_value, max_value
)

print("Изменённая матрица:")
for row in matrix:
    print(row)
