import java.util.Arrays;

public class Sudoku {

    public class TestCase {
        String dataLine;
        int[][] matrix;

        public TestCase(String dataLine) {
            this.dataLine = dataLine;
        }

    }

    
    public static void main(String[] args) {
        
    }
    
    public static int[][] parse(String dataLine) {
        int[][] matrix = new int[9][9];
        int i = 0;
        int j = 0;
        for (int stringIndex = 0; stringIndex < dataLine.length(); stringIndex++) {
            i++;
            j++;
            if (stringIndex % 9 == 0) {
                i = 0;
                j = 0;
            }
            matrix[i][j] = (int)dataLine.charAt(stringIndex);
        }
    
        return matrix;
    }
    
    public static String matrixString(int[][] matrix) {
        String out = "";
        for (int i = 0; i < matrix.length; i++) {
            out += Arrays.toString(matrix[i]);
        }
        return out;
    }
}
