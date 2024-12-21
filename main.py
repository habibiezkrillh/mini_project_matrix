from matrix_operation import input_matrix, print_matrix, add_matrices, subtract_matrices, multiply_matrices, determinant, inverse

def main():
    print("Operasi Matriks 4x4 Max")
    print("1. Penjumlahan Matrix")
    print("2. Pengurangan Matrix")
    print("3. Perkalian Matrix")
    print("4. Determinan Matrix")
    print("5. Inverse Matrix")
    choice = int(input("Pilih operasi (1-5): "))

    if choice in [1, 2, 3]:
        rows1 = int(input("Masukkan jumlah baris matriks pertama: "))
        cols1 = int(input("Masukkan jumlah kolom matriks pertama: "))
        matrix1 = input_matrix(rows1, cols1)

        rows2 = int(input("Masukkan jumlah baris matriks kedua: "))
        cols2 = int(input("Masukkan jumlah kolom matriks kedua: "))
        matrix2 = input_matrix(rows2, cols2)

        if choice == 1:
            result = add_matrices(matrix1, matrix2)
        elif choice == 2:
            result = subtract_matrices(matrix1, matrix2)
        else:
            result = multiply_matrices(matrix1, matrix2)

        print("Hasil operasi: ")
        print_matrix(result)

    elif choice == 4:
        size = int(input("Masukkan ukuran matriks persegi (n x n): "))
        matrix = input_matrix(size, size)
        det = determinant(matrix)
        print(f"Determinan matriks: {det}")

    elif choice == 5:
        size = int(input("Masukkan ukuran matriks persegi (n x n): "))
        matrix = input_matrix(size, size)
        try:
            inv = inverse(matrix)
            print("Invers Matriks: ")
            print_matrix(inv)
        except ValueError as e:
            print(e)
    
    else:
        print("Pilihan anda tidak valid, mohon untuk pilih nomor yang sesuai")

if __name__ == "__main__":
    main()