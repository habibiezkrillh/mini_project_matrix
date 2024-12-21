def input_matrix(rows, cols): # Fungsi ini untuk menerima input matriks dari user
    print(f"Masukkan elemen matriks {rows}x{cols}: ")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Baris {i+1}: ").split()))
        while len(row) != cols:
            print("Jumlah elemen tidak sesuai! coba lagi.")
            row = list(map(int, input(f"Baris {i+1}: ").split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix): # Fungsi ini untuk mencetak matriks ke layar (screen)
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(matrix1, matrix2): # Fungsi untuk operasi Penjumlahan Matriks
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2): # Fungsi untuk operasi Pengurangan Matriks
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2): # Fungsi untuk perkalian matriks
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def determinant(matrix): # Fungsi untuk operasi Determinan matriks
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3:
        return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
                - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
                + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

def inverse(matrix): # Fungsi untuk operasi Invers Matriks
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinan bernilai 0.")
    if len(matrix) == 2:
        return [[matrix[1][1] / det, -matrix[0][1] / det],
                [-matrix[1][0] / det, matrix[0][0] / det]]
    elif len(matrix) == 3:
        adj = [[((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])) / det,
                -((matrix[0][1] * matrix[2][2]) - (matrix[0][2] * matrix[2][1])) / det,
                ((matrix[0][1] * matrix[1][2]) - (matrix[0][2] * matrix[1][1])) / det],
               [-((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0])) / det,
                ((matrix[0][0] * matrix[2][2]) - (matrix[0][2] * matrix[2][0])) / det,
                -((matrix[0][0] * matrix[1][2]) - (matrix[0][2] * matrix[1][0])) / det],
               [((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0])) / det,
                -((matrix[0][0] * matrix[2][1]) - (matrix[0][1] * matrix[2][0])) / det,
                ((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])) / det]]
        return adj