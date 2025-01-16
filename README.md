# Sparse Matrix Operations

## Overview
The **Sparse Matrix Operations** program is a Python-based implementation for manipulating sparse matrices. It includes functions to convert dense matrices to sparse representation, compute transpose, add matrices, and perform matrix multiplication.

## Features
- **Convert Dense to Sparse:** Efficiently converts a dense matrix to a sparse representation using a dictionary.
- **Sparse Transpose:** Computes the transpose of a sparse matrix.
- **Sparse Addition:** Adds two sparse matrices if their dimensions match.
- **Sparse Multiplication:** Multiplies two sparse matrices if their dimensions are compatible.
- **Random Sparse Matrix Generator:** Generates random sparse matrices for testing.

## Installation
To run this project, ensure you have **Python 3.x** installed on your system.

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/sparse-matrix-operations.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd sparse-matrix-operations
   ```
3. **Run the script:**
   ```bash
   python SparseMatrix.py
   ```

## Usage
1. The program includes the following primary functions:
   - `dense_to_sparse(matrix)`: Converts a dense matrix (list of lists) to a sparse representation.
   - `sparse_transpose(sp_matrix)`: Computes the transpose of a sparse matrix.
   - `sparse_add(sp_matrix1, sp_matrix2)`: Adds two sparse matrices.
   - `sparse_multiply(sp_matrix1, sp_matrix2)`: Multiplies two sparse matrices.
2. Users can modify or add test cases in the `main()` function to test different operations.
3. Running the script displays the results of various sparse matrix operations.

## Example Output
```
Dense Matrix 1:
[[0, 0, 5, 0, 0], [0, 2, 0, 4, 0], [7, 0, 0, 0, 3]]
Sparse Matrix 1:
{-1: [3, 5], (0, 2): 5, (1, 1): 2, (1, 3): 4, (2, 0): 7, (2, 4): 3}
Sparse Transpose:
{-1: [5, 3], (2, 0): 5, (1, 1): 2, (3, 1): 4, (0, 2): 7, (4, 2): 3}
Addition Result:
{-1: [3, 5], (0, 2): 10, (1, 1): 4, (1, 3): 8, (2, 0): 14, (2, 4): 6}
Multiplication Result:
{-1: [3, 2], (0, 1): 28, (1, 0): 21, (2, 1): 35}
```

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.

