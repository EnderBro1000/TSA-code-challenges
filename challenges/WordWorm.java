import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class WordWorm {

    public static class TestCase {
        public char[][] wordMap;
        public String[] wordBank;
        public boolean[] wordFound; // boolean list in the same order as wordBank list

        public TestCase(char[][] wordMap, String[] wordBank) {
            this.wordMap = wordMap;
            this.wordBank = wordBank;

            wordFound = new boolean[wordBank.length];
            for (int i = 0; i < wordFound.length; i++) {
                wordFound[i] = false;
            }
        }

        // sets wordFound boolean list to the solved answer
        public void solve() {
            // choose a word to search for (looping through map once PER word)      Note: searching for every word at once would not work (at least without an alphabetical search process on the bank itself), as words can have the same starting letters. Or the same 3 letters before a difference, etc.   
            //  loop through every cell
            //  start recursive search when first letter of word is found.
            //      follow recursion with continuing letters, spawning recursion at each up/down/left/right/DIAGONALLY with matching letter for the word.
            //      set wordFound  =  true for the found word if recursion reaches the end of the word
                        // break out of recursion as that word has been found (don't keep searching)
            //      keep wordFound = false for the found word if recursion doesn't reach the end of the word.
            for (int wordBankIndex = 0; wordBankIndex < wordBank.length; wordBankIndex++) {
                String word = wordBank[wordBankIndex];
                char firstLetter = word.charAt(0);
                for (int row = 0; row < wordMap.length; row++) {
                    for (int col = 0; col < wordMap[0].length; col++) {
                        if (wordMap[row][col] == firstLetter) {
                            //System.out.println("Started search for \"" + word + "\" at row:" + row + " col:" + col);
                            search(word, wordBankIndex, row, col, 1);
                        }
                    }
                }
            }
        }

        // recursive search
        private void search(String word, int wordBankIndex, int row, int col, int letterIndex) {
            if (letterIndex >= word.length()) wordFound[wordBankIndex] = true; // the word is found when every letter has been reached
            if (wordFound[wordBankIndex]) return; // if word is found, end the search for it. This is a separate if statement to check if other branches have completed the search

            char targetLetter = word.charAt(letterIndex);

            //System.out.println("Search spawned\tat row:" + row + " col:" + col);

            // row - 1  & col       -> up
            // row + 1  & col       -> down

            // row      & col - 1   -> left
            // row      & col + 1   -> right

            // row - 1 & col - 1    -> upLeft
            // row - 1 & col + 1    -> downRight
            // row + 1 & col - 1    -> downLeft
            // row + 1 & col + 1    -> downRight            

            // domain:
            // 0 <= row + i < wordMap.length
            // 0 <= col + j < wordMap[0].length


            for (int i = -1; i <= 1; i++) { // loop surrounding rows
                int targetRow = row + i;

                if (targetRow >= 0 && targetRow < wordMap.length) { // if rows in domain
                    for (int j = -1; j <= 1; j++) { // loop surrounding cols
                        if (!(i == 0 && j == 0)) { // if target is moved from current position
                            int targetCol = col + j;
    
                            if (targetCol >= 0 && targetCol < wordMap[0].length) { // if cols in domain
                                if (wordMap[targetRow][targetCol] == targetLetter) { // if letter matches target 
                                    search(word, wordBankIndex, targetRow, targetCol, letterIndex + 1); // continue search
                                }
                            }
                        }
                    }

                }
            }
            //System.out.println("Search died\tat row:" + row + " col:" + col);
            // no word found by this branch if code reached here
        }

        // must first run solve() to get and store the result.
        public void printResult() {
            for (int i = 0; i < wordBank.length; i++) {
                if (wordFound[i]) System.out.println(wordBank[i]);
            }
        }

        // toString() used for debugging
        public String toString() {
            String out = "\n";
            // wordMap
            for (int row = 0; row < wordMap.length; row++) {
                out += englishList(charConvert(wordMap[row]), "", " ", "") + "\n";
            }

            out += Arrays.toString(wordBank); // word bank
            return out + "\n";
        }

        // convert primitive char list to Character object list
        private static Character[] charConvert(char[] charArray) {
            Character[] objectArray = new Character[charArray.length];
            for (int i = 0; i < objectArray.length; i++) {
                objectArray[i] = (Character)charArray[i];
            }
            return objectArray;
        }
    }

    public static void main(String[] args) {
        String[] lines = inLinesToString(); // take standard input
        //String[] lines = fileLinesToString("word-worm-input.txt");

        TestCase[] testCases = getTestCases(lines); // parse the input

        // for (TestCase testCase : testCases) {
        //     System.out.println(testCase);
        // }

        for (TestCase testCase : testCases) { 
            testCase.solve(); // solve the test case
            testCase.printResult(); // display the results
        }
    }

    // get each test case's word map and word bank from input.
    public static TestCase[] getTestCases(String[] inputLines) {
        TestCase[] cases = new TestCase[Integer.parseInt(inputLines[0])];

        int lineNumber = 1;
        for (int caseNumber = 0; caseNumber < cases.length; caseNumber++) {
            // get word map
            String[] rowCol = inputLines[lineNumber].split(" ");
            int rows = Integer.parseInt(rowCol[0]);
            int cols = Integer.parseInt(rowCol[1]);

            lineNumber++; // increment line number each time a line is read to move forward in the input independent of cases.

            char[][] wordMap = new char[rows][cols];
            for (int row = 0; row < wordMap.length; row++, lineNumber++) {
                wordMap[row] = getCharsLine(inputLines[lineNumber]); // each row is a char array of the map's letters.
            }

            // get word bank
            int amountOfWords = Integer.parseInt(inputLines[lineNumber]);
            String[] wordBank = new String[amountOfWords];
            
            lineNumber++;

            for (int i = 0; i < wordBank.length; i++, lineNumber++) {
                wordBank[i] = inputLines[lineNumber];
            }

            // create and store the TestCase
            cases[caseNumber] = new TestCase(wordMap, wordBank);
        }

        return cases;
    }

    // converts string to char array after removing string spaces 
    public static char[] getCharsLine(String line) {
        String noSpaces = "";
        for (int i = 0; i < line.length(); i++) {
            char letter = line.charAt(i);
            if (letter != ' ') noSpaces += letter;
        }
        return noSpaces.toCharArray();
    }

    // standard input: converts System.in input (file) to a String array, where each element is one line in the file.
    public static String[] inLinesToString() {
        Scanner input = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<String>();
        while(input.hasNextLine()) {
            lines.add(input.nextLine());
        }
        input.close();
        String[] linesArray = new String[lines.size()];
        linesArray = lines.toArray(linesArray);
        return linesArray;
    }

    // turns a list into a String with formatting: StartItemSplitItemEnd. Used for debugging
    public static <T> String englishList(T[] list, String start, String split, String end) {
        String str = start;

        for (int i = 0; i < list.length; i++) {
            str += list[i].toString();
            if (i != list.length-1) {
                str += split;
            }
        }
        str += end;

        return str;
    }

    // gets a scanner from a File at path. Used for debugging
    public static Scanner getScanner(String path) {
        try{
            return new Scanner(new File(path));
        } catch (FileNotFoundException e){
            System.out.println("EXCEPTION: File not found at path (when constructing scanner): " + path);
            e.printStackTrace();
        } catch (Exception e) {
            System.out.println("EXCEPTION: getScanner exception");
            e.printStackTrace();
        }
        return null;
    }

    // converts a File at path to a String array, where each element is one line in the file. Used for debugging
    public static String[] fileLinesToString(String path) {
        Scanner input = getScanner(path);
        ArrayList<String> lines = new ArrayList<String>();
        while(input.hasNextLine()) {
            lines.add(input.nextLine());
        }
        input.close();
        String[] linesArray = new String[lines.size()];
        linesArray = lines.toArray(linesArray);
        return linesArray;
    }
}