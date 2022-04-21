import java.util.Arrays;
import java.util.Random;


public class QuickSort {
    public static Random rand;

    public static void main(String[] args) {
        int[] input = {5, 10, 1, 3, 6, 2, 0};

        rand = new Random();
        System.out.println(Arrays.toString(Sort(input)));
    }

    public static int randInt(int min, int max) {
        return rand.nextInt(max) + min;
    }

    
    public static int[] Sort(int[] input) {
        int i = randInt(0, input.length);
        int compareVal = input[i];

        for (int j = 0; j < input.length; j++) {
            //if (j == i) continue;

            // swap values across
            if (input[j] < compareVal && j > i) {
                // sending compareVal forward
                for (int k = i; k < j; k++) {
                    int temp = input[k+1];
                    input[k+1] = input[k];
                    input[k] = temp;
                }
            } else if (input[j] > compareVal && j < i) {
                // sending compareVal backward
                for (int k = i; k > j; k--) {
                    int temp = input[k-1];
                    input[k-1] = input[k];
                    input[k] = temp;
                }
            }
        }

        if (!isSorted(input)) Sort(input);

        return input;
    }

    public static boolean isSorted(int[] input) {
        for(int i = 0; i < input.length-1; i++) {
            if (input[i] > input[i+1]) return false;
        }
        return true;
    }
}
/*
            for (int j = 0; j < input.length; j++) {
                int compareVal = input[j];

                if (compareVal < testVal) {
                    // move test val rightward
                    int temp = input[i+1];
                    input[i+1] = input[i];
                    input[i] = temp; 
                }
            }
*/