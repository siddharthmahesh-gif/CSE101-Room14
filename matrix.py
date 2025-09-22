def isXMatrix(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True

# Get matrix size from user
n = int(input("Enter the size of the square matrix: "))

# Initialize an empty matrix
grid = []

print("Enter the rows of the matrix, with elements separated by spaces:")

for _ in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        print(f"Error: Each row must have {n} elements.")
        exit()
    grid.append(row)

# Check if it is an X-Matrix
if isXMatrix(grid):
    print("True - The matrix is an X-Matrix.")
else:
    print("False - The matrix is NOT an X-Matrix.")