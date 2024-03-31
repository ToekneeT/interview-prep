import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
public class Search {

    public static void linSearch(ArrayList<String> words, String target) {
        boolean found = false;
        int index = 0;
        // Used to calculate elapsed time.
        long finish = 0;
        long start = System.nanoTime();
        for (int i = 0; i < words.size(); i++) {
            if (words.get(i).equals(target)) {
                finish = System.nanoTime();
                index = i;
                found = true;
                break;
            }
        }
        System.out.println("Linear Search:");
        if (found) {
            System.out.printf("%s found at index %d\n", target, index);
            double elapsedTimeInMilliseconds = (double) (finish - start) / 1_000_000;
            System.out.printf("Elapsed time: %.2f\n\n", elapsedTimeInMilliseconds);
            return;
        }
        System.out.printf("%s not found in word file.\n\n", target);
    }

    public static void indexOf(ArrayList<String> words, String target) {
        long start = System.nanoTime();
        int indexOf = words.indexOf(target);
        long finish = System.nanoTime();
        System.out.println("Index of:");
        if (indexOf != -1) {
            System.out.printf("%s found at index %d\n", target, indexOf);
            double elapsedTimeInMilliseconds = (double) (finish - start) / 1_000_000;
            System.out.printf("Elapsed time: %.2f\n\n", elapsedTimeInMilliseconds);
            return;
        }
        System.out.printf("%s not found in word file.\n\n", target);
    }

    public static void binarySearch(ArrayList<String> words, String target) {
        long start = System.nanoTime();
        long finish = 0;
        int low = 0;
        int high = words.size() - 1;
        System.out.println("Binary Search:");

        while (low <= high) {
            int mid = (low + high) / 2;
            if (words.get(mid).equals(target)) {
                finish = System.nanoTime();
                System.out.printf("%s found at index %d\n", target, mid);
                double elapsedTimeInMilliseconds = (double) (finish - start) / 1_000_000;
                System.out.printf("Elapsed time: %.2f\n\n", elapsedTimeInMilliseconds);
                return;
            }
            if (words.get(mid).compareTo(target) < 0) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        System.out.printf("%s not found in word file.\n\n", target);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a word to search: ");
        String lookup = input.nextLine().toLowerCase();
        // Stick the words in the word file into an arraylist.
        ArrayList<String> words = new ArrayList<>();
        try {
            File w = new File("words_alpha.txt");
            Scanner reader = new Scanner(w);
            while (reader.hasNextLine()) {
                words.add(reader.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error has occurred.");
            e.printStackTrace();
        }

        while (!lookup.equals("quit program")) {
            linSearch(words, lookup);
            indexOf(words, lookup);
            binarySearch(words, lookup);
            System.out.println("Enter a word to search: ");
            lookup = input.nextLine().toLowerCase();
        }

    }
}