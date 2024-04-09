// This Matrix class stores 2D matrices in row-major notation. Example:
// 3 4 2 1
// 5 1 2 3
// Expected 1D array: {3, 4, 2, 1, 5, 1, 2, 3}
public class Matrix {
    int numOfRows, numOfCol, matrixSize;
    int[] matrixArr;

    // Default constructor creates a 3x1 order.
    public Matrix() {
        numOfRows = 3;
        numOfCol = 3;
        matrixSize = numOfRows * numOfCol;
        matrixArr = new int[matrixSize];
    }

    // Creates an empty array with rows and columns specified by the user.
    public Matrix(int numOfRows, int numOfCol) {
        if (numOfRows <= 0 || numOfCol <= 0) {
            throw new IllegalArgumentException("One or more arguments is less than or equal to 0.");
        }
        this.numOfRows = numOfRows;
        this.numOfCol = numOfCol;
        matrixSize = numOfRows * numOfCol;
        matrixArr = new int[matrixSize];
    }

    // Passing an array to the Matrix class will result in a default of 1 x matrixSize until specified. Example:
    // 3 4 2 1
    // Expected 1D array: {3, 4, 2, 1}
    public Matrix(int[] arr) {
        matrixSize = arr.length;
        numOfRows = 1;
        numOfCol = matrixSize;
        matrixArr = arr;
    }

    public int size() {
        return matrixSize;
    }

    public int columns() {
        return numOfCol;
    }

    public int rows() {
        return numOfRows;
    }

//    // Need to fix. Prevent from going over number of elements in array. Divisible by columns?
//    public void setNumOfRows(int rows) {
//        numOfRows = rows;
//    }
//
//    // Need to fix. Prevent from going over number of elements in array. Divisible by rows?
//    public void setNumOfCol(int col) {
//        numOfCol = col;
//    }

    public void changeDimensions(int rows, int col) {
        if (rows * col > matrixSize) {
            throw new IllegalArgumentException("New dimensions larger than current size of matrix dimensions.");
        }
        numOfRows = rows;
        numOfCol = col;
    }

    // Adds two matrices together. Has to be of equal length, otherwise throws an execption.
    public Matrix add(Matrix m) {
        if (matrixSize != m.matrixSize) {
            throw new ArrayIndexOutOfBoundsException("Array sizes do not match.");
        }
        int[] newArr = new int[matrixSize];
        for (int i = 0; i < matrixSize; i++) {
            newArr[i] = matrixArr[i] + m.matrixArr[i];
        }
        Matrix newMatrix = new Matrix(newArr);
        newMatrix.numOfRows = numOfRows;
        newMatrix.numOfCol = numOfCol;
        newMatrix.matrixSize = matrixSize;
        return newMatrix;
    }

    // Add to an element at an index.
    public Matrix add(int index, int num) {
        if (index >= matrixSize || index < 0) {
            throw new ArrayIndexOutOfBoundsException("Index out of bounds.");
        }
        matrixArr[index] += num;
        Matrix newMatrix = new Matrix(matrixArr);
        newMatrix.numOfRows = numOfRows;
        newMatrix.numOfCol = numOfCol;
        newMatrix.matrixSize = matrixSize;
        return newMatrix;
    }

    public int get(int index) {
        if (index >= matrixSize || index < 0) {
            throw new ArrayIndexOutOfBoundsException("Index out of bounds.");
        }
        return matrixArr[index];
    }

    public void set(int index, int num) {
        if (index >= matrixSize || index < 0) {
            throw new ArrayIndexOutOfBoundsException("Index out of bounds.");
        }
        matrixArr[index] = num;
    }

//    public void remove(int index) {
//        if (matrixSize <= index) {
//            throw new ArrayIndexOutOfBoundsException("Index out of bounds.");
//        }
//        int[] newArr = new int[matrixSize - 1];
//        for (int i = 0; i < matrixSize - 1; i++) {
//            if (index == 0) {
//                newArr[i] = matrixArr[i + 1];
//            }
//            else if (i == index && index != 0) {
//                newArr[i] = matrixArr[i + 1];
//            }
//            else if (i != index) {
//                newArr[i] = matrixArr[i];
//            }
//        }
//    }

    public void print() {
        for(int i = 0; i < matrixSize; i++) {
            if (i % numOfCol == 0 && i != 0) {
                System.out.println();
            }
            if ((i + 1) % numOfCol == 0) {
                System.out.print(matrixArr[i]);
            }
            else {
                System.out.print(matrixArr[i] + " ");
            }
        }
        System.out.println();
    }
}
