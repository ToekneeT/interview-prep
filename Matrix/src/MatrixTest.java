import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class MatrixTest {

    @Test
    void testRow() {
        Matrix m = new Matrix(1, 2);
        assertEquals(1, m.rows());
    }

    @Test
    void testCol() {
        Matrix m = new Matrix(1, 2);
        assertEquals(2, m.columns());
    }

    @Test
    void testMatrixSize() {
        Matrix m = new Matrix(2, 5);
        assertEquals(10, m.size());
    }

    @Test
    void testSize() {
        Matrix m = new Matrix(1, 2);
        assertEquals(2, m.size());
    }

//    @Test
//    void test_printSameRowSize() {
//        Matrix m = new Matrix(3, 3);
//        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
//        System.setOut(new PrintStream(outContent));
//        String expectedOutput = "0" + System.lineSeparator() + "0" + System.lineSeparator() + "0" +
//                System.lineSeparator();
//        m.print();
//        assertEquals(expectedOutput, outContent.toString());
//    }

    @Test
    void testPrint3x4() {
        Matrix m = new Matrix(3, 4);
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        String expectedOutput = "0 0 0 0" + System.lineSeparator() + "0 0 0 0" + System.lineSeparator() +
                "0 0 0 0" + System.lineSeparator();
        m.print();
        assertEquals(expectedOutput, outContent.toString());
    }

    @Test
    void testPrint2x2() {
        Matrix m = new Matrix(2, 2);
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        String expectedOutput = "0 0" + System.lineSeparator() + "0 0" + System.lineSeparator();
        m.print();
        assertEquals(expectedOutput, outContent.toString());
    }

    @Test
    void testPrintPassedArr() {
        Matrix m = new Matrix(new int[]{3, 4, 2, 1});
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        String expectedOutput = "3 4 2 1" + System.lineSeparator();
        m.print();
        assertEquals(expectedOutput, outContent.toString());
    }

    @Test
    void testRowZero() {
        Throwable exception = assertThrows(IllegalArgumentException.class, () -> {
                Matrix m = new Matrix(0, 1);
            }
        );
        assertEquals("One or more arguments is less than or equal to 0.", exception.getMessage());
    }

    @Test
    void testColZero() {
        Throwable exception = assertThrows(IllegalArgumentException.class, () -> {
                Matrix m = new Matrix(2, 0);
            }
        );
        assertEquals("One or more arguments is less than or equal to 0.", exception.getMessage());
    }

    @Test
    void testGet() {
        Matrix m = new Matrix(new int[]{1, 2, 3});
        assertEquals(3, m.get(2));
    }
    @Test
    void testAddAtIndex() {
        Matrix m = new Matrix(2, 3);
        m.add(2, 5);
        assertEquals(5, m.get(2));
    }

    @Test
    void testAddNegativeAtIndex() {
        Matrix m = new Matrix(2, 3);
        m.add(1, -2);
        assertEquals(-2, m.get(1));
    }

    @Test
    void testInvalidArrSizeAdd() {
        Matrix m = new Matrix(2, 3);
        Matrix m2 = new Matrix(2, 4);
        Throwable exception = assertThrows(ArrayIndexOutOfBoundsException.class, () -> {
                m.add(m2);
            }
        );
        assertEquals("Array sizes do not match.", exception.getMessage());
    }

    @Test
    void testAddTwoArrays() {
        Matrix m = new Matrix(new int[]{3, 4, 2, 1});
        Matrix m2 = new Matrix(new int[]{5, 1, 2, 3});
        Matrix m3 = m.add(m2);
        int[] expectedArr = new int[]{8, 5, 4, 4};
        assertEquals(true, Arrays.equals(m3.matrixArr, expectedArr));
    }

    @Test
    void testAddNegativeIndex() {
        Matrix m = new Matrix(2, 3);
        Throwable exception = assertThrows(ArrayIndexOutOfBoundsException.class, () -> {
                    m.add(-1, 5);
                }
        );
        assertEquals("Index out of bounds.", exception.getMessage());
    }

    @Test
    void testAddOverIndex() {
        Matrix m = new Matrix(2, 3);
        Throwable exception = assertThrows(ArrayIndexOutOfBoundsException.class, () -> {
                    m.add(6, 5);
                }
        );
        assertEquals("Index out of bounds.", exception.getMessage());
    }

    @Test
    void testSet() {
        Matrix m = new Matrix(2, 3);
        m.set(1, 5);
        assertEquals(5, m.get(1));
        assertEquals(0, m.get(0));
    }

    @Test
    void testGetNegativeIndex() {
        Matrix m = new Matrix(2, 3);
        Throwable exception = assertThrows(ArrayIndexOutOfBoundsException.class, () -> {
                m.get(-1);
            }
        );
        assertEquals("Index out of bounds.", exception.getMessage());
    }

    @Test
    void testGetOverIndex() {
        Matrix m = new Matrix(2, 3);
        Throwable exception = assertThrows(ArrayIndexOutOfBoundsException.class, () -> {
                    m.get(6);
                }
        );
        assertEquals("Index out of bounds.", exception.getMessage());
    }

    @Test
    void testSetNegativeIndex() {
        Matrix m = new Matrix(2, 3);
        Throwable exception = assertThrows(ArrayIndexOutOfBoundsException.class, () -> {
                    m.set(-2, 5);
                }
        );
        assertEquals("Index out of bounds.", exception.getMessage());
    }

    @Test
    void testSetOverIndex() {
        Matrix m = new Matrix(2, 3);
        Throwable exception = assertThrows(ArrayIndexOutOfBoundsException.class, () -> {
                    m.set(10, 1);
                }
        );
        assertEquals("Index out of bounds.", exception.getMessage());
    }

    @Test
    void testChangeDimensions() {
        Matrix m = new Matrix(2, 3);
        m.changeDimensions(3, 2);
        assertEquals(3, m.rows());
        assertEquals(2, m.columns());
    }

    @Test
    void testInvalidChangeDimensions() {
        Matrix m = new Matrix(2, 3);
        Throwable exception = assertThrows(IllegalArgumentException.class, () -> {
                m.changeDimensions(3, 3);
            }
        );
        assertEquals("New dimensions larger than current size of matrix dimensions.", exception.getMessage());
    }
//    @Test
//    void testRemove() {
//        Matrix m = new Matrix(new int[]{1, 2, 3});
//        m.remove(0);
//        int[] expectedArr = new int[]{2, 3};
//        assertEquals(true, Arrays.equals(m.matrixArr, expectedArr));
//        assertEquals(2, m.get(0));
//    }
}
