class SparseMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        transposed = [[self.matrix[j][i] for j in range(rows)] for i in range(cols)]
        self.matrix = transposed

    def change_element(self, row, col, value):
        self.matrix[row][col] = value

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = input(f"Enter the elements of row {i+1} separated by spaces: ").split()
    matrix.append([int(x) for x in row])

sparse = SparseMatrix(matrix)
row, col, value = map(int, input("Enter row, column, and new value to change an element (separated by spaces): ").split())
sparse.change_element(row, col, value)
sparse.transpose()
print("Transposed matrix with changed element:", sparse.matrix)
